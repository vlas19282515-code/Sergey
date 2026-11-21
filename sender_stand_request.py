# Власов Сергей, 49-когорта, Финальный проект

import requests
import configuration


def create_order(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body
    )


def get_order_by_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
        params={"t": track}
    )