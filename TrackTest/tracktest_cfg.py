import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

### conditions
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'START61_V11::All'

### standard includes
process.load('Configuration/StandardSequences/Services_cff')
process.load('Configuration.StandardSequences.Geometry_cff')
process.load("Configuration.StandardSequences.RawToDigi_cff")
process.load("Configuration.EventContent.EventContent_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")

process.load("RecoTracker.TrackProducer.TrackRefitters_cff")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/relval/CMSSW_6_2_0_pre2-PU_START61_V11/RelValTTbar/GEN-SIM-RECO/v1/00000/FE48CBD7-437A-E211-AE8D-003048F1CA6E.root',
    '/store/relval/CMSSW_6_2_0_pre2-PU_START61_V11/RelValTTbar/GEN-SIM-RECO/v1/00000/F600059F-2E7A-E211-9399-003048F1186A.root',
    '/store/relval/CMSSW_6_2_0_pre2-PU_START61_V11/RelValTTbar/GEN-SIM-RECO/v1/00000/76BF1027-B17A-E211-92CC-003048F00AF8.root',
    '/store/relval/CMSSW_6_2_0_pre2-PU_START61_V11/RelValTTbar/GEN-SIM-RECO/v1/00000/6C0AE730-317A-E211-8416-003048F0E00A.root',
    '/store/relval/CMSSW_6_2_0_pre2-PU_START61_V11/RelValTTbar/GEN-SIM-RECO/v1/00000/22D46130-377A-E211-81F5-003048F0258A.root',
    '/store/relval/CMSSW_6_2_0_pre2-PU_START61_V11/RelValTTbar/GEN-SIM-RECO/v1/00000/0E566081-337A-E211-9E7F-003048CF97B2.root',
    '/store/relval/CMSSW_6_2_0_pre2-PU_START61_V11/RelValTTbar/GEN-SIM-RECO/v1/00000/0A6F8ADE-2D7A-E211-BE3D-0025901D5E20.root'
    )
)

process.select = cms.EDFilter('TrackSelector',
        src = cms.InputTag('TrackRefitter'),
        #cut = cms.string("quality('highPurity') & (algo=9 ) & abs(eta)<0.9")
        #cut = cms.string("quality('highPurity') & (algo=10) & abs(eta)<0.9")
        #cut = cms.string("quality('highPurity') & (algo=9 ) & abs(eta)>0.9 & abs(eta)<1.6")
        #cut = cms.string("quality('highPurity') & (algo=10) & abs(eta)>0.9 & abs(eta)<1.6")
        #cut = cms.string("quality('highPurity') & (algo=9 ) & abs(eta)>1.6 & abs(eta)<2.5")
        cut = cms.string("quality('highPurity') & (algo=10) & abs(eta)>1.6 & abs(eta)<2.5")
)

process.demo = cms.EDAnalyzer('TrackTest',
        tracks = cms.untracked.InputTag('select'),
        TTRHBuilder = cms.string('WithAngleAndTemplate'),
        saveHists = cms.bool(True),
        printInfo = cms.bool(False)
)

process.TFileService = cms.Service("TFileService", 
        #fileName = cms.string("histo_algo09_00eta09.root"),
        #fileName = cms.string("histo_algo10_00eta09.root"),
        #fileName = cms.string("histo_algo09_09eta16.root"),
        #fileName = cms.string("histo_algo10_09eta16.root"),
        #fileName = cms.string("histo_algo09_16eta25.root"),
        fileName = cms.string("histo_algo10_16eta25.root"),
        closeFileFast = cms.untracked.bool(True)
)

process.p = cms.Path(process.TrackRefitter*process.select*process.demo)
