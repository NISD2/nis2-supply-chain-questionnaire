# BSI NIS-2 Lieferketten-Checkliste — inverse mapping

Customer-facing view: given a Baustein from the [BSI NIS-2 Lieferketten-Checkliste v1.0 (5 June 2025)](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/NIS-2/nis-2-lieferkette_grundschutz-checkliste.pdf), which questionnaire fields help satisfy it.

Generated from `data/supplier-questionnaire.json`. Do not edit by hand. Re-run `scripts/generate-bsi-mapping.py` after editing field tags.

**Coverage:** 46 Bausteine, 72 field-mappings, 56 fields total.

## ASST — Asset-Schnittstellen / Datenuebertragung

| Baustein | Fields |
|----------|--------|
| `ASST.4.A1` | `hasAssetInventory` |

## BES.1 — Beschaffungsmanagement Grundlagen

| Baustein | Fields |
|----------|--------|
| `BES.1.A2` | `legalName`, `registeredAddress`, `country`, `primaryDomain`, `tagline` |

## BES.2 — Bedarf

| Baustein | Fields |
|----------|--------|
| `BES.2.A1` | `serviceDescription` |
| `BES.2.A2` | `country`, `dataProcessingLocations`, `notifyOnLocationChange`, `saasHostingRegion` |

## BES.3 — Lieferantenauswahl

| Baustein | Fields |
|----------|--------|
| `BES.3.A1` | `isSaas`, `isOnPrem`, `isProfessionalServices`, `isManagedService` |
| `BES.3.A2` | `description`, `serviceDescription` |

## BES.4 — Vertragskriterien

| Baustein | Fields |
|----------|--------|
| `BES.4.A2` | `securityPolicyReviewedAnnually` |
| `BES.4.A4.1` | `mfaEnforcedInternal`, `saasMfaEnforced` |
| `BES.4.A4.3` | `onPremSignedReleases` |
| `BES.4.A5` | `hasIsms` |
| `BES.4.A6` | `hasPenetrationTestingProgram` |
| `BES.4.A6.1` | `hasIso27001OrEquivalent` |
| `BES.4.A6.2` | `bsiRegistrationId` |
| `BES.4.A7` | `backgroundChecks`, `proServicesBackgroundCheckScope` |

## BES.5 — Vertragsinhalte

| Baustein | Fields |
|----------|--------|
| `BES.5.A11` | `staffSecurityTraining` |
| `BES.5.A12` | `proServicesNdaInPlace` |
| `BES.5.A13` | `notifyMaterialChanges` |
| `BES.5.A14` | `notifyMaterialChanges` |
| `BES.5.A15` | `hasIncidentResponsePlan` |
| `BES.5.A15.1` | `securityContactName`, `incidentContactEmail`, `incidentContactPhone` |
| `BES.5.A15.2` | `incidentSlaHours`, `pastBreachesDisclosed` |
| `BES.5.A15.3` | `vulnerabilityHandling`, `onPremPatchSlaCriticalHours` |
| `BES.5.A15.3.1` | `onPremVulnerabilityDisclosurePolicy` |
| `BES.5.A15.5` | `incidentAssistanceCommitment` |
| `BES.5.A16` | `acceptRightToAudit` |
| `BES.5.A2` | `saasRtoHours`, `managedOnCall24x7` |
| `BES.5.A3` | `cooperateWithAuthorities` |
| `BES.5.A4` | `managedSessionRecording` |
| `BES.5.A5` | `dpaAvailable` |
| `BES.5.A7` | `hasPrivilegedAccessMgmt`, `proServicesCustomerPremisesPolicy`, `managedPrivilegedAccessMgmt` |
| `BES.5.A8` | `hasSubprocessors`, `subprocessorList` |
| `BES.5.A9` | `subprocessorList` |

## BES.6 — Vertragsende

| Baustein | Fields |
|----------|--------|
| `BES.6.A1` | `hasExitPlan` |
| `BES.6.A2` | `dataReturnOnTermination` |
| `BES.6.A4` | `dataReturnOnTermination` |

## BES.7 — Abnahme

| Baustein | Fields |
|----------|--------|
| `BES.7.A7` | `onPremSbomProvided` |
| `BES.7.A7.1` | `onPremSbomProvided` |

## BES.8 — Resilience / Notfallvorsorge

| Baustein | Fields |
|----------|--------|
| `BES.8.A1` | `hasExitPlan` |
| `BES.8.A2` | `hasBusinessContinuityPlan` |
| `BES.8.A3` | `hasBusinessContinuityPlan` |

## DEV.6 — Software-Entwicklung — SBOM

| Baustein | Fields |
|----------|--------|
| `DEV.6.A3` | `onPremSbomProvided` |

## DLS.2 — Dienstleistersteuerung — laufende Pruefung

| Baustein | Fields |
|----------|--------|
| `DLS.2.A1` | `hasIsms` |
| `DLS.2.A1.1` | `bsiRegistrationId`, `hasIso27001OrEquivalent` |

## DLS.5 — Dienstleistersteuerung — Schutzmassnahmen

| Baustein | Fields |
|----------|--------|
| `DLS.5.A10` | `hasCryptographyPolicy`, `saasEncryptionAtRest` |
| `DLS.5.A9` | `hasCryptographyPolicy`, `saasEncryptionInTransit` |

## DLS.6 — Dienstleistersteuerung — Cloud-Profil

| Baustein | Fields |
|----------|--------|
| `DLS.6.A1` | `dataProcessingLocations`, `isSaas`, `saasHostingRegion` |
