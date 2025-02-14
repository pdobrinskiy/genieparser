expected_output = {
    "GigabitEthernet1/0/16":{
        "service_policy":{
            "output":{
                "policy_name":{
                    "WIRED-EGRESS-POLICY":{
                        "queue_stats_for_all_priority_classes":{
                            "priority_level":{
                                "1":{
                                    "queueing":True
                                },
                                "2":{
                                    "queueing":True
                                }
                            }
                        },
                        "class_map":{
                            "AutoQos-4.0-Output-Multimedia-Conf-Queue":{
                                "match_evaluation":"match-any",
                                "packets":0,
                                "match":[
                                    "dscp af41 (34) af42 (36) af43 (38)",
                                    "cos  4"
                                ],
                                "priority":{
                                    "percent":20,
                                    "kbps":200000,
                                    "burst_bytes":5000000
                                },
                                "priority_level":2
                            }
                        }
                    }
                }
            }
        }
    }
}
