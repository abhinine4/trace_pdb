# `trace_pdb`

mini python debugger using trace functions

================
# `breakpoint()`

- replacement for `pdb.set_trace()`; PEP 553
- calls the breakpoint hook
- set by `PYTHONBREAKPOINT`; default: pdb.set_trace

================
# Trace functions

- hooks for debuggers
- **global** trace function:
    - called when entering new scope
    - _can_ return local trace function
    - set via `sys.settrace(some_callable)`
- **local** trace function:
    - called at certain other events

================
# Events

- `call`
- `line`
- `return` (`arg`: return value)
- `exception` (`arg`: exception tuple)
- `opcode`*

================
# Frames
≈ entries on the call stack

- current code object
- current file with line number
- current locals, globals
- parent frame

================

- set a global trace function with `sys.settrace`
- have it return a local trace function
- events: `call`, `line`, `return`, `exception`
- frames: interpreter state with
    - .f_lineno
    - .f_code
    - .f_trace
    - .f_back
