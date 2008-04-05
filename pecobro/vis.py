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
                          lineWidth=kr.map.linear(kr.map.expr('1.0'),
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
