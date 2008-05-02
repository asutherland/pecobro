def file_overview(caboodle, file_or_path):
    import visophyte.kora as kr
    import math

    layout = kr.map.Graphviz(nodeId=None,
                             nodeEdges=kr.map.expr('ever_called.items()'),
                             prog='fdp',
                             #prog='neato',
                             #nodeEdges=kr.map.expr('invocations'),
                             edgeNode=kr.map.expr('0')
                             )
    
    BLACK = kr.raw.color('black')
    
    circ = kr.vis.Circle(#fill=kr.map.distinct_color(kr.map.expr('filename'),
                         #                           s=0.2),
                         fill=kr.map.hsv(hue=kr.map.distinct_value_exclusive(kr.map.expr('base_name')),
                                         saturation=kr.map.linear(kr.map.expr('exclusive_weight'),
                                                                  output_low=0.0,
                                                                  output_high=1.0),
                                         value=0.9,
                                         alpha=0.625),
                         stroke=BLACK, strokeWidth=1,
                         radius=30,
                         label=kr.map.expr('base_name'),
                         link=kr.map.expr('@'),
                         )
    
    map_time_angle = kr.map.linear(None,
                                   output_low=-math.pi/2,
                                   output_high=math.pi*3/2) 
    
    rings = kr.vis.Rings(vis=circ,
                         data=kr.map.expr('invocations'),
                         radius=40,
                         thickness=kr.map.linear(kr.map.expr('3'),
                                                 output_low=16,
                                                 output_high=4),
                         startAng=map_time_angle(kr.map.expr('1')),
                         endAng=map_time_angle(kr.map.expr('2')),
                         # er, since we are just cheating to use the depth, just use that
                         fill=kr.map.distinct_color(kr.map.expr('3'),
                                                    s=0.6, v=0.9),
                         #stroke=BLACK,
                         stroke=kr.map.distinct_color(kr.map.expr('3'),
                                                    s=0.9, v=0.6),
                         # eh, just link to the source_file.
                         )
    
    func_vis = circ
    
    graph_vis = kr.vis.Graphito(
                          nodes=kr.map.expr('@'),
                          y=layout.y,
                          x=layout.x,
                          nodeVis=func_vis,
                          #lineColor=kr.map.distinct_color(kr.map.expr('name')),
                          #lineColor=kr.raw.color('black'),
                          lineColor=kr.map.rgba(r=0, g=0, b=128,
                                               a=kr.map.linear(
                                                    kr.map.expr('1.1'),
                                                    output_low=16,
                                                    output_high=128)),
                          #lineWidth=4,
                          lineWidth=kr.map.log(kr.map.expr('1.0'),
                                                  output_low=1.0,
                                                  output_high=8.0),
                          nodeId=None,
                          nodeEdges=kr.map.expr('ever_called.items()'),
                          #nodeEdges=kr.map.expr('invocations'),
                          edgeNode=kr.map.expr('0')
                          )
    
    vis = kr.vis.Pad(graph_vis,
                     padLeft=15, padTop=15, padRight=15, padBottom=15)
    
    context = kr.feed.native(caboodle.relevant_source_files).make_context()
    
    kr.render.use_renderer('svg')
    kr.render.contextualize(context, kr.themes.default)
    
    WIDTH, HEIGHT = 640, 640
    model = vis.topRender(context,
                      width=WIDTH, height=HEIGHT,
                      )
    
    def link_source_file(source_file, xobj):
        xobj.set('id', 'vis|%s' % (source_file.norm_base_name,))
        xobj.set('class', 'vsf')
    
    kr.render.renderToFile(model, file_or_path,
                           linker=link_source_file,
                           width=WIDTH, height=HEIGHT)

def func_time_slices(function, width=640, height=24, mode='sparkline'):
  try:
    import visophyte.kora as kr
    import math
    
    max_time_value = float(function.file.caboodle.max_time_value)
    
    if mode == 'sparkline':
        PIX_PER_HORIZ_POINT = 3
    elif mode == 'smooshline':
        PIX_PER_HORIZ_POINT = 1
    
    horiz_points = width / PIX_PER_HORIZ_POINT
    time_per_horiz_point = max_time_value / horiz_points 
    
    active_points = [0.0] * horiz_points
    inactive_points = [0.0] * horiz_points
    
    for invoc in function.invocations:
        first_range_beg = int(invoc.t_start / time_per_horiz_point)
        last_range_beg = int((invoc.t_end - 1) / time_per_horiz_point) + 1
        
        # flag if this invocation is happening inside a call to this function
        # (indirectly recursive works too, not just directly recursive) 
        recursive_invoc = False
        ancestor = invoc.parent
        while ancestor is not None:
            if ancestor.func == function:
                recursive_invoc = True
                break
            else:
                ancestor = ancestor.parent
        
        for cur_range in range(first_range_beg, last_range_beg):
            r_start = cur_range * time_per_horiz_point
            r_stop  = r_start + time_per_horiz_point
            
            tr_start = max(r_start, invoc.t_start)
            tr_stop  = min(r_stop, invoc.t_end)
            
            # slice must be in [0.0, 1.0]
            slice = (tr_stop - tr_start) / time_per_horiz_point
            active_points[cur_range] += slice
            if recursive_invoc:
                inactive_points[cur_range] -= slice
            
            for call in (invoc.calls or ()):
                cr_start = max(r_start, call.t_start)
                cr_stop  = min(r_stop, call.t_end)
                
                # don't let negatives sneak in...
                if cr_stop < cr_start:
                    continue
                
                # call_slice must be in [0.0, 1.0]
                call_slice = (cr_stop - cr_start) / time_per_horiz_point
                # this transfers from active to inactive; no net increase
                active_points[cur_range] -= call_slice
                inactive_points[cur_range] += call_slice
    
    data = zip(active_points, inactive_points)

    vis = kr.vis.BarChart(style=mode,
                          values=(kr.map.constant_scale(height, kr.map.expr('0')),
                                  kr.map.constant_scale(height, kr.map.expr('1'))),
                          positions=('above', 'above'),
                          fill=(kr.raw.color('#ee6666'),
                                kr.raw.color('#66ee66')),
                          )
    
    context = kr.feed.native(data).make_context()
    
    kr.render.use_renderer('svg')
    kr.render.contextualize(context, kr.themes.default)
    
    model = vis.topRender(context,
                      width=width, height=height,
                      )
    
    return kr.render.renderToImageString(model, 'svg',
                                         width=width, height=height)
  except:
    pass
    
