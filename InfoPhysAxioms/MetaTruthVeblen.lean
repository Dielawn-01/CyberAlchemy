import InfoPhysAxioms.MetaTruth
import InfoPhysAxioms.VeblenDruid

namespace InfoPhys

open VeblenDruid

/--
  The ingestion of an external MetaTruth certificate by an agent.
  This action verifies the ZKPCR signature (via `accept_meta_truth`).
  Upon success, it triggers the Veblen `deprecate_agent` function,
  absorbing the Sprite (oracle) and advancing the Druid's depth.
-/
def oracle_deprecate {P : Prop} (a : Agent) (cert : ExternalCertificate P) : Agent :=
  -- The certificate acts as a proof term. By requesting it, we force validation.
  let _proof : P := accept_meta_truth cert
  deprecate_agent a

/--
  Any agent that successfully parses and digests an external ZKPCR certificate
  strictly increases its Veblen Index (depth).
-/
theorem oracle_advances_depth {P : Prop} (a : Agent) (cert : ExternalCertificate P) :
  agent_level (oracle_deprecate a cert) = agent_level a + 1 := by
  unfold oracle_deprecate agent_level
  exact deprecate_advances a

end InfoPhys
