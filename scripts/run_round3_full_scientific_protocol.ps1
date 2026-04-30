param(
  [string]$Out = "runs/round3_scientific_full",
  [string]$LatentDims = "150,64,32,16,8",
  [string]$EvalSeeds = "76,77,78,79,80,81,82,83,84,85",
  [int]$Episodes = 50,
  [int]$EpisodeSteps = 1000,
  [int]$BenchmarkSteps = 5000,
  [int]$MigrationSteps = 1000,
  [double]$EquivalenceThreshold = 0.90,
  [switch]$Force
)

$ErrorActionPreference = "Stop"

$Repo = Split-Path -Parent $PSScriptRoot
Set-Location $Repo
$env:PYTHONPATH = Join-Path $Repo "src"

Write-Host "Repo: $Repo"
Write-Host "PYTHONPATH: $env:PYTHONPATH"
python -c "import wormsim; print('wormsim:', wormsim.__file__)"

$argsList = @(
  "scripts/run_round3_full_scientific_protocol.py",
  "--out", $Out,
  "--train-tasks", "food,harm,wall",
  "--validation-tasks", "dynamic_food,time_harm",
  "--heldout-tasks", "memory,switch,hard_mixed",
  "--episodes", "$Episodes",
  "--episode-steps", "$EpisodeSteps",
  "--benchmark-steps", "$BenchmarkSteps",
  "--migration-steps", "$MigrationSteps",
  "--latent-dims", $LatentDims,
  "--train-seed", "1",
  "--eval-seeds", $EvalSeeds,
  "--equivalence-threshold", "$EquivalenceThreshold"
)

if ($Force) {
  $argsList += "--force"
}

python @argsList 2>&1 | Tee-Object -FilePath (Join-Path $Out "protocol.log")

$Summary = Join-Path $Out "round3_scientific_summary.md"
Write-Host "\n--- SUMMARY ---"
Get-Content $Summary

$Zip = "$Out/results_bundle.zip"
Compress-Archive -Path (Join-Path $Out "*") -DestinationPath $Zip -Force
Write-Host "\nDONE. Paste the summary above or send: $Zip"
