from WMCore.Configuration import Configuration
import os

# get parameters from submit script
productionlabel = os.environ['CRAB_PRODUCTIONLABEL']
dataset         = os.environ['CRAB_DATASET']
outputsite      = os.environ['CRAB_OUTPUTSITE']
outputdir       = os.environ['CRAB_OUTPUTDIR']
conffile        = os.environ['CRAB_CONFFILE']
outputfile      = 'nanodqmio.root'
if 'CRAB_OUTPUTFILE' in os.environ.keys(): outputfile = os.environ['CRAB_OUTPUTFILE']
lumimask        = None
if 'CRAB_LUMIMASK' in os.environ.keys(): lumimask = os.environ['CRAB_LUMIMASK']
lumisperjob     = 10
if 'CRAB_LUMISPERJOB' in os.environ.keys(): lumisperjob = int(os.environ['CRAB_LUMISPERJOB'])

# process the dataset name
datasetparts = dataset.split('/')
pd = datasetparts[1]
era = datasetparts[2]
dtier = datasetparts[3]
requestname = era + '_' + productionlabel

# get CMSSW release
cmssw_base = os.environ['CMSSW_BASE']

# set work area
workarea = os.path.join(cmssw_base, 'src/crab', productionlabel, pd)

# format pyCfgParams argument
pycfgparams = ['outputFile='+outputfile, 'inputFile='+dataset, 'nEvents=-1']

# print all configurable arguments
print('INFO from crabconf.py')
print('Found following arguments:')
print('  productionlabel = {}'.format(productionlabel))
print('  dataset = {}'.format(dataset))
print('  outputsite = {}'.format(outputsite))
print('  outputdir = {}'.format(outputdir))
print('  conffile = {}'.format(conffile))
print('  outputfile = {}'.format(outputfile))
print('  lumimask = {}'.format(lumimask))
print('  lumisperjob = {}'.format(lumisperjob))
print('  requestname = {}'.format(requestname))
print('  cmssw_base = {}'.format(cmssw_base))
print('  workarea = {}'.format(workarea))

# initialize crab configuration
config = Configuration()

# general settings
config.section_('General')
config.General.transferLogs            = True
config.General.requestName             = requestname
config.General.workArea                = workarea

# job type settings
config.section_('JobType')
config.JobType.psetName                = conffile
config.JobType.pyCfgParams             = pycfgparams
config.JobType.pluginName              = 'analysis'
config.JobType.outputFiles             = [outputfile]
config.JobType.sendExternalFolder      = True
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores                = 1
config.JobType.maxMemoryMB             = 5000

# data settings
config.section_('Data')
config.Data.inputDataset               = dataset
config.Data.unitsPerJob                = lumisperjob
config.Data.splitting                  = 'LumiBased'
#config.Data.outLFNDirBase              = outputdir
config.Data.publication                = False
#config.Data.lumiMask                   = lumimask
config.Data.allowNonValidInputDataset  = True
config.Data.inputBlocks                = [
                             #'/Muon0/Run2023C-v1/RAW#6122e527-a414-4a70-8391-9cff26fadd5d',
                             #'/Muon0/Run2023C-v1/RAW#7bdcea05-a01c-4583-b428-20f69589ade4',
                             #'/Muon0/Run2023C-v1/RAW#9d44d568-a7d5-4a5b-8aa1-799697d1aa0e',
                             #'/Muon0/Run2023C-v1/RAW#ef400e67-986d-4c61-a075-b3691b419770',
                             #'/Muon0/Run2023C-v1/RAW#6925a080-249e-45ca-a1fc-a6a6ee68a7ab',
                             #'/Muon0/Run2023C-v1/RAW#8f77b126-16ad-4000-b9d5-a40cf8bebd0b',
                             #'/Muon0/Run2023D-v1/RAW#88a5d235-80d3-4c56-802c-6f433d810b29'

                             '/Muon1/Run2023C-v1/RAW#3eeffcab-8401-4d4c-a7ef-117bc9632ba2',
                             '/Muon1/Run2023C-v1/RAW#50813b06-e8e7-47ad-bfef-693173ca4b0c',
                             '/Muon1/Run2023C-v1/RAW#ed4d4a84-fcc6-43b0-ab28-aa048a344dc7',
                             '/Muon1/Run2023C-v1/RAW#18d53df6-34bb-4506-88c5-8c62a6a11a5e',
                             '/Muon1/Run2023C-v1/RAW#2abe0f31-f04d-4920-8883-db3c4a9a258b',
                             '/Muon1/Run2023C-v1/RAW#84e4c183-9958-4c6b-9223-d1614283fe97',
                             '/Muon1/Run2023C-v1/RAW#8bedb6e9-e42c-4e12-827e-379610049c14',
                             #'/Muon1/Run2023D-v1/RAW#7b7e1551-937d-46f9-863b-86bda8198083'

                             #'/ZeroBias/Run2023C-v1/RAW#3812b8b1-8941-484f-b4b7-6e67fc4331fa',
                             #'/ZeroBias/Run2023C-v1/RAW#8eaffa39-24bd-489e-a6b2-6c92b7c1892f',
                             #'/ZeroBias/Run2023C-v1/RAW#e030016f-a83e-43af-b37a-ae0ec8b5a9a5',
                             #'/ZeroBias/Run2023C-v1/RAW#e4fef9b4-b718-4a78-84dc-c79027ea7f3b',
                             #'/ZeroBias/Run2023D-v1/RAW#c6750448-0de0-4b7e-a269-8c3ea9a85972',
                             #'/ZeroBias/Run2023D-v1/RAW#1b0e7d1a-2add-4066-8057-e3c209213dbe'
                                         ]

# site settings
config.section_('Site')
config.Site.storageSite                = outputsite
