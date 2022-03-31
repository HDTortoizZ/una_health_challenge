from django.forms import Form, MultipleChoiceField, IntegerField
from upload.models import GlucoseLevels


def get_user_id_list():
    glucose_lvls = GlucoseLevels.objects.all()
    print(glucose_lvls)
    user_ids = list()
    for item in glucose_lvls:
        user_ids.append(item.user_id)
    glucose_lvls = sorted(set(user_ids))
    return [(str(item), item) for item in glucose_lvls]


def get_timestamp_list():
    glucose_lvls = GlucoseLevels.objects.all()
    timestamps = list()
    for item in glucose_lvls:
        timestamps.append(item.timestamp)
    timestamps = sorted(set(timestamps))
    return [(str(item), item) for item in timestamps]


sort_choices = [(0, 'user_id'), (1, 'device'), (2, 'serial_number'), (3, 'timestamp'),
                (4, 'glucose_value_history'), (5, 'glucose_levels')]


def filter_form_gen():
    while True:
        class FilterForm(Form):
            user_id = MultipleChoiceField(label='Please enter a user_id', choices=get_user_id_list())
            timestamp = MultipleChoiceField(label='Please enter a timestamp', choices=get_timestamp_list())
            sort = MultipleChoiceField(label='sort by', choices=sort_choices)
            max_rows = IntegerField(label='select the maximum number of displayed rows', min_value=1)
        yield FilterForm