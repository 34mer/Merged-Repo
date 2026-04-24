import Lake
open Lake DSL

package ProjectX where

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "master"

@[default_target]
lean_lib ProjectX

lean_exe projectx_check where
  root := `ProjectXCheck
