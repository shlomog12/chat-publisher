

class Survey:

    def __init__(self, survey_id:str, survey_name:str, survey_description:str, options:[str], is_multiple_choice:bool):
        self._survey_id = survey_id
        self._survey_name = survey_name
        self._survey_description = survey_description
        self._options = options
        self._is_multiple_choice = is_multiple_choice

    def get_survey_id(self) -> str:
        return self._survey_id

    def get_survey_name(self) -> str:
        return self._survey_name

    def get_survey_description(self) -> str:
        return self._survey_description

    def get_options(self) -> [str]:
        return self._options

    def get_is_multiple_choice(self) -> bool:
        return self._is_multiple_choice

    def __str__(self) -> str:
        survey_str = f'{self._survey_id} name: {self._survey_name} description: {self._survey_description}, is_multiple_choice: {self._is_multiple_choice}'
        for i in range(len(self._options)):
            survey_str += f' option {i+1}: {self._options[i]}'
        return survey_str