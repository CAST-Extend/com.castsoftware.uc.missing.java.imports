import cast_upgrade_1_6_13 # @UnusedImport
import cast.analysers.jee
from cast.analysers import log

class MissingImportsAnalysis(cast.analysers.jee.Extension): 
    def __init__(self):
        self.java_parser = None
        
        self.intermediateFile = None
        self.NbImports = 0
    
    @cast.Event('com.castsoftware.internal.platform', 'jee.java_parser')
    def receive_java_parser(self, parser):
        self.java_parser = parser
        log.info('Java Parser Received')
    
    def start_analysis(self, options):
        log.info('Starting Missing Java Import Analysis...')
        self.intermediateFile = self.get_intermediate_file("missingJavaImports.txt")
    
    def end_analysis(self):
        log.info('Import identified: %d' % self.NbImports)
             
    def start_type(self, _type):        
        #log.info("Parse file %s" % _type.get_position().get_file().get_path())
        all_tokens = self.java_parser.parse(_type.get_position().get_file().get_path())
        if all_tokens is not None:
            allImports = all_tokens.imports
            for imp in allImports:
                log.info('%s;%s;%s\n' % (_type.get_typename(), _type.get_fullname(), imp.get_name()))
                self.intermediateFile.write('%s;%s;%s\n' % (_type.get_typename(), _type.get_fullname(), imp.get_name()))
                self.NbImports += 1

     
            