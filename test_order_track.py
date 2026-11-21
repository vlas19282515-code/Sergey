# Власов Сергей, 49-когорта, Финальный проект
import sender_stand_request
import data


def test_get_order_by_track_returns_200():
    create_response = sender_stand_request.create_order(data.order_body)
    assert create_response.status_code == 201, (
        "Ожидался код 201, получен " + str(create_response.status_code) +
        ". Тело: " + create_response.text
    )

    track = create_response.json().get("track")
    assert track is not None, "В ответе отсутствует поле track"

    get_response = sender_stand_request.get_order_by_track(track)
    assert get_response.status_code == 200, (
        "Ожидался код 200, получен " + str(get_response.status_code) +
        ". Тело: " + get_response.text
    )