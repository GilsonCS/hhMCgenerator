from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'Radion_hh_wwww_jets_MiniAOD'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'B2G-RunIISummer16MiniAODv2_Radion_hh_wwww_MiniAOD_cfg.py'
config.JobType.numCores = 4
#config.JobType.maxMemoryMB = 5000

config.Data.inputDataset = '/MinBias/bregnery-Radion_hh_wwww_jets_AODSIM-b1a4edca9adfa7a2e4059536bf605cd7/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/user/bregnery/' 
config.Data.publication = True
config.Data.outputDatasetTag = 'Radion_hh_wwww_jets_MiniAOD'

config.Site.storageSite = 'T3_US_FNALLPC'