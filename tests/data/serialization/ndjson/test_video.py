import json

from labelbox.data.serialization.ndjson.converter import NDJsonConverter


def test_video():
    with open('tests/data/assets/ndjson/video_import.json', 'r') as file:
        data = json.load(file)

    res = NDJsonConverter.deserialize(data).as_list()
    res = list(NDJsonConverter.serialize(res))
    assert res == [data[2], data[0], data[1], data[3], data[4], data[5]]
