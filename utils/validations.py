
class Validator:
    @staticmethod
    def is_blank(var):
        '''checks if any required field is blank'''
        if var.strip() == '':
            return 'All fields are required'
        return None