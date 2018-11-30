import os
import os.path
import sys
import inspect
import __main__
from datetime import datetime


class MAD:
    """ "Model and Dependencies" - capture machine learning model 
            settings and dependencies:

        0) Create a model_logs directory if it does not exist, and 
            save log files with a time stamp (or not) to that directory.
        1) Document the machine learning model name and it's non-default parameters.
        2) Document the version of python in use.
        3) Document the pip requirements.
        4) Document the necessary imports.
        5) Document any other important notes not covered above, 
            such as how missing values were filled, etc.
    """

    def __init__(self, mod, 
        file_name='model_data.txt', extra_notes='', add_time_stamp=True, **WTL):
        """Perform setups for auto documentation.
        
        The first line captures the filename of the script instantiating this class.
        The second line captures the locals from the same script in the first step.
        The if block adds a time stamp to the default, or provided, file_name.
        The next if block adds a model logs directory IF it does not yet exist.
        The file open to write context manager then creates a time stamped file,
            if add_time_step is true, and adds a documentation section captured 
            from each method.

        Arguments:
            mod {class instance} --  instance of machine learning class
        
        Keyword Arguments:
            file_name {str} -- the filename used for the log file 
                (default: {'model_data.txt'})
            extra_notes {str} -- optional notes providing mode detail 
                (default: {''})
            add_time_stamp {bool} -- boolean to add timp stamp to model file or not 
                (default: {True})
            WTL {kwargs} -- What To Log (WTL) are key word arguments for what to log. 
                The default is to log everything. Pass any py_version=False, 
                pip_requirements=False, imports=False, and/or capture_notes=False 
                to NOT log one or more of these.
        """
        # Section A.1
        self.calling_file = __main__.__file__
        self.locals = inspect.currentframe().f_back.f_locals
        if add_time_stamp == True:
            time_date = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            file_name = file_name.replace(
                file_name[-4:], '_' + time_date + file_name[-4:])

        # Section A.2
        if not os.path.exists('model_logs'):
            os.makedirs('model_logs')

        # Section A.3
        with open('./model_logs/' + file_name, 'w') as self.out_file:
            self.out_file.write(self.get_model_info(mod))
            if (('py_version' not in WTL) or (WTL['py_version'] == True)): 
                self.out_file.write(self.get_python_version())
            if (('pip_requirements' not in WTL) or (WTL['pip_requirements'] == True)): 
                self.out_file.write(self.get_pip_requirements())
            if (('imports' not in WTL) or (WTL['imports'] == True)): 
                self.out_file.write(self.get_necessary_imports())
            if (('capture_notes' not in WTL) or (WTL['capture_notes'] == True)): 
                self.out_file.write('\n' + '# Extra Notes:\n' + extra_notes)

    def _get_model_string(self, model):
        """Internal function that returns a string of the full model call

        Arguments:
            :param model: the instance of the model class being used
        Returns:
            a string of the full model call
        """
        model_string   = str(model).replace('\n', '').replace(' ', '')

        return model_string
        
    def _get_model_name(self, model_string):
        """Internal function to get the model name
        Arguments:
            :param model_string: a string of the instance and model parameters
        Returns:
            {str} the model name
        """
        model_name = model_string.split('(')[0]

        return model_name

    def _get_model_params_array(self, model_string):
        """docstring here
        Arguments:
            :param model_string: the string of the instance call of the model class
        Returns:
            {list} a list of the model instance parameters
        """
        model_name = self._get_model_name(model_string)
        model_params_array = model_string.replace(
            model_name,'').replace('(','').replace(')','').split(',')

        return model_params_array

    def get_model_info(self, mod):
        """Simple class method to return a formatted string of model information.
        Arguments:
            :param mod: {class instance} -- argument passed from __init__ method
        Returns:
            {str} the model with non default parameters in use
        """
        # Section B.1: get the model string and parameters
        model_string = self._get_model_string(mod)
        if 'Pipeline' in model_string:
            model_string = model_string.replace(',',',\n\t\t')
            return '# Model and parameters:\n\t' + model_string + '\n'

        model_name   = self._get_model_name(model_string)
        model_params = self._get_model_params_array(model_string)
        
        # Section B.2a: get the params used in the default instance of the model
        default_imports_array  = [
            x for x in self._get_imports_array() if model_name in x]
        default_imports_string = "\n".join(default_imports_array)
        default_exec_command   = default_imports_string + ";" + "mod_default=" \
            + model_name + "()"
        exec(default_exec_command, globals(), locals())
        # Section B.2b: get the default model string and parameters
        default_model_string = self._get_model_string(locals()['mod_default'])
        default_model_params = self._get_model_params_array(default_model_string)

        # Section B.3: get the list of non default parameters and create a model string 
        #     with non default parameters
        non_default_model_params = [
            x for x in model_params if x not in default_model_params]
        if len(non_default_model_params) == 0:
            log_model_string = model_name + "()"    
        else:
            log_model_string = model_name \
                + "(\n\t\t" + "\n\t\t".join(non_default_model_params) + ")"

        return '# Model and parameters:\n\t' + log_model_string + '\n'

    def get_python_version(self):
        """Simple class method to return a string of python version information.
        """
        return '\n# python version:\n' + str(sys.version.split('\n')[0] + '\n')

    def get_pip_requirements(self):
        """Class method to capture pip requirements for the script.
        
        The first code block creates a string out of the local items. 
        The second block does a pip version flexible import of freeze to capture 
            modules loaded by pip.
        The third block obtains all pip installs that appear in local items also
            and puts them in a data frame.
        The fourth block formats a requirements.txt style string of required
            pip modules needed by the script instantiating this class.
        
        Returns:
            {str} -- a formatted list of modules needing pip installation for the 
                        model to work.
        """
        # Section C.1
        local_modules_string = str(self.locconvals.items())

        # Section C.2
        try:
            from pip._internal.operations import freeze
        except ImportError:  # pip < 10.0
            from pip.operations import freeze

        # Section C.3
        x = freeze.freeze()
        pip_list = []
        for p in x:
            line = p.split('==')
            if line[0] in local_modules_string:
                pip_list.append(line)

        # Section C.4
        pip_rqmts = '\n# pip requirements:\n'
        for row in pip_list:
            line_string = row[0] + '==' + row[1] + '\n'
            pip_rqmts += line_string

        return pip_rqmts

    def _get_imports_array(self):
        """Returns an array of import statements from the calling file.
        """   
        with open(self.calling_file, 'r') as f:
            FLA = f.readlines()
            imprt_lines = [line.rstrip('\n') for line in FLA if (
                ('import ' in line) and
                ('#' != line[0]) and ('MAD' not in line))]

        return imprt_lines
        
    def get_necessary_imports(self):
        """Returns a formatted string of imports needed by the script 
            instantiating this class.

        The first code block reads the file instantiating this class, and
            filters a list of the file lines to find those containing 
            import statements.
        The second code block prepares a formatted string for return of 
            the imports captured in the first block.

        Returns:
            {str} -- a formatted list of imports from the script of 
                        code block one.
        """
        # Section D.1
        imprt_lines = self._get_imports_array()

        # Section D.2
        imports_string = '\n# Necessary Imports:\n'
        for line in imprt_lines:
            imports_string += line + '\n'

        return imports_string
