#!/usr/sbin/dtrace -Zs
/* We want to know the stack depth and vtimestamp spans for each call.
   For each call we also want to know what file and function we are dealing
   with.  However, we don't really need to know that every time if it's
   faster to provide some shorter unique id.  (For now we assume that the
   id effort is just as expensive because it would be all hashy.)

   We do not care about the cpu identifier for now because it is my
   understanding that javascript execution is currently single-threaded
   for mozilla.
 */

/* do not output any info other than what we want */
#pragma D option quiet

/* we need large buffers */
#pragma D option bufsize=16m

dtrace:::BEGIN
{
}

/* get the probes flagged as enabled... */
/*
javascript$target::jsdtrace_function_entry:function-entry
{
}

javascript$target::jsdtrace_function_return:function-return
{
}
*/

struct stack_info {
    uint64_t vtick;
    int lineno;
    string run_filename;
    int run_lineno;
};

self int depth[unsigned long];
self struct stack_info si[unsigned long, int];

javascript$target:::function-info
{
    this->cx = arg6;
    /* function-entry probe args: filename, class name, function name */
    /* function-info adds: line number, dfp filename, dfp line number*/
    self->depth[this->cx]++;
    this->depth = self->depth[this->cx];
    
    self->si[this->cx, this->depth].vtick  = vtimestamp;
    self->si[this->cx, this->depth].lineno = arg3;
    self->si[this->cx, this->depth].run_filename = basename(copyinstr(arg4));
    self->si[this->cx, this->depth].run_lineno = arg5;
}

javascript$target:::function-return
{
    this->cx = arg3;
    this->depth = self->depth[this->cx];
    /* probe args: filename, class name, function name*/
    /* note that non-chrome filenames have some weird symlink-style thing
       going on... basename at least disambiguates this for us. */
    this->filename = basename(copyinstr(arg0));
    this->objname = copyinstr(arg1);
    this->funcname = copyinstr(arg2);
    printf("r,%x,%x,%x,%x,%s,%s,%s,%d,%s,%d\n", this->cx, this->depth,
           self->si[this->cx, this->depth].vtick, vtimestamp,
           this->filename, this->objname, this->funcname,
           self->si[this->cx, this->depth].lineno,
           self->si[this->cx, this->depth].run_filename,
           self->si[this->cx, this->depth].run_lineno);
    /* clean up */
    self->depth[this->cx]--;
}

wavascript$target:::function-info
{
    /* function-entry probe args: filename, class name, function name */
    /* function-info adds: line number, dfp filename, dfp line number*/
    printf("w,%s,%s,%s,%d,%s,%d\n", basename(copyinstr(arg0)),
           copyinstr(arg1), copyinstr(arg2),
           arg3, basename(copyinstr(arg4)), arg5);
}

wavascript$target:::function-return
{
    printf("b,%s,%s,%s\n", basename(copyinstr(arg0)), copyinstr(arg1), copyinstr(arg2));
}

javascript$target:::execute-start
{
    printf("e,%s,%d\n", copyinstr(arg0), arg1);
}

javascript$target:::execute-done
{
    printf("x,%s,%d\n", copyinstr(arg0), arg1);
}

