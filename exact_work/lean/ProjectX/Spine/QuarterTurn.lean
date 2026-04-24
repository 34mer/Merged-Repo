import ProjectX.Basic

namespace ProjectX

/-- Left index of the active adjacent pair. -/
def leftIdx {m : Nat} (i : Fin m) : Fin (m + 1) := Fin.castSucc i

/-- Right index of the active adjacent pair. -/
def rightIdx {m : Nat} (i : Fin m) : Fin (m + 1) := i.succ

/-- Local `A₂` quarter-turn transport on an ordered family of size `m+1`.
It sends the active adjacent pair `(f_i, f_{i+1})` to `(f_{i+1}, -f_i)` and leaves all
other coordinates unchanged. -/
def quarterTurn {α : Type _} [Neg α] {m : Nat} (i : Fin m)
    (f : Fin (m + 1) → α) : Fin (m + 1) → α :=
  Function.update
    (Function.update f (leftIdx i) (f (rightIdx i)))
    (rightIdx i) (-f (leftIdx i))

@[simp] theorem quarterTurn_left {α : Type _} [Neg α] {m : Nat} (i : Fin m)
    (f : Fin (m + 1) → α) :
    quarterTurn i f (leftIdx i) = f (rightIdx i) := by
  simp [quarterTurn, leftIdx, rightIdx]

@[simp] theorem quarterTurn_right {α : Type _} [Neg α] {m : Nat} (i : Fin m)
    (f : Fin (m + 1) → α) :
    quarterTurn i f (rightIdx i) = -f (leftIdx i) := by
  simp [quarterTurn, leftIdx, rightIdx]

theorem quarterTurn_other {α : Type _} [Neg α] {m : Nat} (i : Fin m)
    (f : Fin (m + 1) → α) (k : Fin (m + 1))
    (hkL : k ≠ leftIdx i) (hkR : k ≠ rightIdx i) :
    quarterTurn i f k = f k := by
  simp [quarterTurn, hkL, hkR]

@[simp] theorem quarterTurn_sq_left {α : Type _} [Neg α] {m : Nat} (i : Fin m)
    (f : Fin (m + 1) → α) :
    quarterTurn i (quarterTurn i f) (leftIdx i) = -f (leftIdx i) := by
  rw [quarterTurn_left, quarterTurn_right]

@[simp] theorem quarterTurn_sq_right {α : Type _} [Neg α] {m : Nat} (i : Fin m)
    (f : Fin (m + 1) → α) :
    quarterTurn i (quarterTurn i f) (rightIdx i) = -f (rightIdx i) := by
  rw [quarterTurn_right, quarterTurn_left]

theorem quarterTurn_sq_other {α : Type _} [Neg α] {m : Nat} (i : Fin m)
    (f : Fin (m + 1) → α) (k : Fin (m + 1))
    (hkL : k ≠ leftIdx i) (hkR : k ≠ rightIdx i) :
    quarterTurn i (quarterTurn i f) k = f k := by
  rw [quarterTurn_other _ _ _ hkL hkR, quarterTurn_other _ _ _ hkL hkR]

end ProjectX
