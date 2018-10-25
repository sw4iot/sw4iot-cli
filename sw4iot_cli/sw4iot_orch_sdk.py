import json

import requests
import urllib3

urllib3.disable_warnings()


class Sw4iotOrchSdk:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def add_slice(self, slice_name):
        r = requests.get('http://{}:{}/orch/add_slice'.format(self.host, self.port), params={
            'slice': slice_name
        }, verify=False)
        response = json.loads(r.content)
        return response if r.status_code == requests.codes.ok else None

    def del_slice(self, slice_name):
        r = requests.get('http://{}:{}/orch/del_slice'.format(self.host, self.port), params={
            'slice': slice_name
        }, verify=False)
        response = json.loads(r.content)
        return response if r.status_code == requests.codes.ok else None

    def get_slices(self):
        r = requests.get('http://{}:{}/orch/get_all_slices'.format(self.host, self.port), verify=False)
        response = json.loads(r.content)
        return response if r.status_code == requests.codes.ok else None

    def get_gateways(self):
        r = requests.get('http://{}:{}/orch/get_all_gw'.format(self.host, self.port), verify=False)
        response = json.loads(r.content)
        return response if r.status_code == requests.codes.ok else None
