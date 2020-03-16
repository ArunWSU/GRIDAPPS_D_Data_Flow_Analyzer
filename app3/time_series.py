# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:17:12 2019

@author: spoudel
"""
import json
import math

class Voltage_Measurements(object):
    """
    WSU VVO
    """
    def __init__(self, msr_mrids_load, sim_output):
        self.meas_load = msr_mrids_load
        self.output = sim_output
        
    def voltage(self):
        data1 = self.meas_load
        data2 = self.output
        # data2 = json.loads(data2.replace("\'",""))
        meas_value = data2['message']['measurements']     
        time_stamp = data2["message"] ["timestamp"]

        data1 = data1['data']
        ds = [d for d in data1 if d['type'] != 'VA']
        out_v = [dict(timestamp=time_stamp)]
        for d1 in ds:                
            if d1['measid'] in meas_value:
                print(d1)
                v = d1['measid']
                volt = meas_value[v]
                # Check phase of load in 9500 node based on last letter
                loadbus = d1['bus']
                phi = (volt['angle'])*math.pi/180
                message = dict(bus = d1['bus'],
                                PNV = [volt['magnitude'], volt['angle']],
                                Phase = d1['phases'], 
                                Measurementid = v)
                out_v.append(message)   
        
        return out_v
