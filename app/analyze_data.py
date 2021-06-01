from database import view
import pandas as pd


# Example data retrieval
def main():

    data = view.all()
    ours_save_file = "./yu_blender_dialogs.csv"
    shirleys_save_file = "./shirley_inspired_dialogs.csv"
    raw_blender_save_file = "./raw_blender_dialogs.csv"
    zhou_save_file = "./zhou_half_half_dialogs.csv"
    user_entity_save_file = "./user_entity_dialogs.csv"

    sum_dialog = {"blue": {"bot": [], "human": []},
                   "cyan": {"bot": [], "human": []},
                   "yellow": {"bot": [], "human": []},
                   "green": {"bot": [], "human": []},
                   "red": {"bot": [], "human": []},}

    sum_surveys = { "pre": {"kind_of_movies": [], "favorite_movies":[], "favorite_actors":[], "favorite_directors":[],},
                    "blue": {"recommend_":[],"preference":[],"consistent":[],"natural":[],"engaging":[],"persuasive":[],"sociable":[],"boring":[],},
                    "cyan": {"recommend_":[],"preference":[],"consistent":[],"natural":[],"engaging":[],"persuasive":[],"sociable":[],"boring":[],},
                    "yellow": {"recommend_":[],"preference":[],"consistent":[],"natural":[],"engaging":[],"persuasive":[],"sociable":[],"boring":[],},
                    "green": {"recommend_":[],"preference":[],"consistent":[],"natural":[],"engaging":[],"persuasive":[],"sociable":[],"boring":[],},
                    "red": {"recommend_":[],"preference":[],"consistent":[],"natural":[],"engaging":[],"persuasive":[],"sociable":[],"boring":[],},
                    "survey_4": {"kind_of_movies": [],}}
    sum_worker_id = []
    sum_blue_length = []
    sum_cyan_length = []
    sum_yellow_length = []
    sum_green_length = []
    sum_red_length = []
    for hit in data:
        if hit.complete:
            # print("Info:", type(hit.info))
            # print("Dialog:", type(hit.dialog))
            # print("Forms:", type(hit.forms))
            bot_names = hit.dialog.keys()
            for bot_name in bot_names:
                sum_dialog[bot_name]["bot"].append(hit.info['worker_id'])
                sum_dialog[bot_name]["human"].append("")
                for turn in hit.dialog[bot_name]:
                    sum_dialog[bot_name]["bot"].append(turn['bot'])
                    sum_dialog[bot_name]["human"].append(turn['human'])
                sum_dialog[bot_name]["bot"].append("")
                sum_dialog[bot_name]["human"].append("")

    df_dialogs_blue = pd.DataFrame(sum_dialog["blue"])
    df_dialogs_cyan = pd.DataFrame(sum_dialog["cyan"])
    df_dialogs_yellow = pd.DataFrame(sum_dialog["yellow"])
    df_dialogs_green = pd.DataFrame(sum_dialog["green"])
    df_dialogs_red = pd.DataFrame(sum_dialog["red"])

    df_dialogs_blue.to_csv(shirleys_save_file)
    df_dialogs_cyan.to_csv(ours_save_file)
    df_dialogs_yellow.to_csv(user_entity_save_file)
    df_dialogs_green.to_csv(zhou_save_file)
    df_dialogs_red.to_csv(raw_blender_save_file)

    def get_form_key(dict_form, form_name):
        for key in dict_form.keys():
            if key in form_name:
                return key
        return None

    for hit in data:
        if hit.complete:
            sum_worker_id.append(hit.info['worker_id'])
            surveys = hit.forms.keys()
            for survey in surveys:
                for survey_q in hit.forms[survey].keys():
                    tmp_survey = sum_surveys[get_form_key(sum_surveys, survey)]
                    if get_form_key(tmp_survey, survey_q):
                        sum_surveys[get_form_key(sum_surveys, survey)][get_form_key(tmp_survey, survey_q)].append(hit.forms[survey][survey_q])
            
            bot_names = hit.dialog.keys()
            for bot_name in bot_names:
                if bot_name == "blue":
                    sum_blue_length.append(len(hit.dialog[bot_name]))
                if bot_name == "cyan":
                    sum_cyan_length.append(len(hit.dialog[bot_name]))
                if bot_name == "yellow":
                    sum_yellow_length.append(len(hit.dialog[bot_name]))
                if bot_name == "green":
                    sum_green_length.append(len(hit.dialog[bot_name]))
                if bot_name == "red":
                    sum_red_length.append(len(hit.dialog[bot_name]))
                
    forms_dict_out = {}
    for survey_key in sum_surveys.keys():
        for q in sum_surveys[survey_key].keys():
            forms_dict_out[survey_key+"_"+q] = sum_surveys[survey_key][q]
    forms_dict_out['worker_id'] = sum_worker_id
    forms_dict_out['blue_length'] = sum_blue_length
    forms_dict_out['cyan_length'] = sum_cyan_length
    forms_dict_out['yellow_length'] = sum_yellow_length
    forms_dict_out['green_length'] = sum_green_length
    forms_dict_out['red_length'] = sum_red_length
    df_forms = pd.DataFrame(forms_dict_out)
    df_forms.to_csv("./surveys.csv")
if __name__ == '__main__':
    main()