from collections import defaultdict


from utils.build_utils import Task, Form


class SurveyJS:

    @classmethod
    def content_to_json(cls, content):
        title = content['title']
        sections = content['data']

        result = {
            'title': title,
            'pages': [

            ],
            "showQuestionNumbers": "off",            
        }

        for section in sections:
            section_title = section['title']
            questions = section['data']

            page = {
                'title': section_title,
                'name': section_title.lower().replace(' ', '_'),
                'questions': [

                ],                
            }

            for question in questions:                
                question_title = question['title']
                required = question['required']
                name = question_title.lower().replace(" ", "_")
                name = ''.join(x for x in name if x.isalpha() or x == '_' or x.isnumeric())
                if question['type'] == 'FreeResponse':
                    page['questions'].append({
                        'type': 'comment',
                        'title': question_title,
                        'name': name,                        
                        'isRequired': required
                    })
                elif question['type'] == 'MultiChoice':
                    page['questions'].append({
                        'type': 'radiogroup',
                        'title': question_title,
                        'name': name,
                        'choices': question['items'],
                        'isRequired': required
                    })
                elif question['type'] == 'CheckBox':
                    page['questions'].append({
                        'type': 'checkbox',
                        'title': question_title,
                        'name': name,
                        'choices': question['items'],
                        'isRequired': required
                    })
                elif question['type'] == 'Likert':
                    page['questions'].append({
                    'type': 'rating',
                    'title': question_title,
                    'name': name,
                    'rateMin': question['min_rating'],
                    'rateMax': question['max_rating'],
                    'minRateDescription': question['min_desc'],
                    'maxRateDescription': question['max_desc'],
                    'isRequired': required
                })

            result['pages'].append(page)

        return {'type': 'form', 'data': result}


class CompileHelper:

    @classmethod
    def layout(cls, task_build):
        result = []
        for element in task_build:      
            if type(element) is Form:
                result.append(SurveyJS.content_to_json(element.content))
            else:
                result.append(element.content)                        
        return result


class Compile:

    def __init__(self, task_build):
        super().__init__()
        self.task_build = task_build  
        self.layout = []                 

    @property
    def task(self):
        self.layout = CompileHelper.layout(self.task_build)
        return self.layout