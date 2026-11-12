import json
from csv_column_select import transform
def test_transform():
 assert transform([{"x":"1","y":"2"}], ["x"]) == [{"x":"1"}]
