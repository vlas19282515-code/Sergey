# Власов Сергей, 49-когорта, Финальный проект
import sender_stand_request
import data


def create_order_and_get_track():
    """Подготовка: создаём заказ и возвращаем его трек."""
    create_response = sender_stand_request.create_order(data.order_body)
    assert create_response.status_code == 201, (
        "Не удалось создать заказ. Код: " + str(create_response.status_code) +
        ". Тело: " + create_response.text
    )
    track = create_response.json().get("track")
    assert track is not None, "В ответе отсутствует поле track"
    return track


def test_get_order_by_track_returns_200():
    """По треку заказа можно получить данные о заказе (код 200)."""
    track = create_order_and_get_track()
    get_response = sender_stand_request.get_order_by_track(track)
    assert get_response.status_code == 200, (
        "Ожидался код 200, получен " + str(get_response.status_code) +
        ". Тело: " + get_response.text
    )