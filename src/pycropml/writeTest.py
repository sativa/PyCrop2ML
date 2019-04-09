# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:46:31 2019

@author: midingoy
"""
from pycropml.render_cyml import Model2Package
from pycropml import render_fortran 
class WriteTest(object):
    def __init__(self, models, language, dir):
        self.models = models
        self.language= language
        self.dir=dir
    
    def write(self):
        """TODO"""
        #code="\n"
        #for model in self.models:
        if self.language=="f90":
            render_fortran.Model2Package(self.models, self.dir).write_tests()
                
        if self.language=="py":
            Model2Package(self.models).write_tests(self.models)+"\n"
        
            
            