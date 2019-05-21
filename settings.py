# замените user, password, ds049945.mongolab.com, example на ваши данные доступа к БД.
MONGO_URI = "mongodb://192.168.99.100:32768/stat-gibdd"

# По умолчанию Eve запускает API в режиме "read-only" (т.е. поддерживаются только GET запросы),
# мы включаем поддержку методов POST, PUT, PATCH, DELETE.
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
    # Описываем ресурс `/users`
    'dtpcards': {
        # Здесь мы описываем модель данных. Для валидации используется модуль Cerberus от автора Eve.
        # Вы можете ознакомиться с ним в официальной документации модуля http://docs.python-cerberus.org/en/stable/.
        # Либо прочитать заметки в официальной документации EVE http://python-eve.org/validation.html#validation.
        'schema': {
            "year": {
                'type': 'string'
            },
            "regioncode": {
                'type': 'string'
            },
            "regionname": {
                'type': 'string'
            },
            "cardid": {
                'type': 'number'
            },
            "rownum": {
                'type': 'number'
            },
            "date": {
                'type': 'string'
            },
            "time": {
                'type': 'string'
            },
            "district": {
                'type': 'string'
            },
            "trafficaccident": {
                'type': 'string'
            },
            "numberdead": {
                'type': 'number'
            },
            "injurednumber": {
                'type': 'number'
            },
            "vehiclenumber": {
                'type': 'number'
            },
            "participantsnumber": {
                'type': 'number'
            },
            "trafficaccidentinfo": {
                "roadnetworkdisadvantages": {
                    'type': 'list'
                },
                "rnobjectta": {
                    'type': 'list'
                },
                "vehicleinfo": {
                    'type': 'list',
                    'default': [],
                    'schema': {
                        "vehiclenumber": {
                            'type': 'string'
                        },
                        "tss": {
                            'type': 'string'
                        },
                        "typevehicle": {
                            'type': 'string'
                        },
                        "brand": {
                            'type': 'string'
                        },
                        "model": {
                            'type': 'string'
                        },
                        "color": {
                            'type': 'string'
                        },
                        "transmissiontype": {
                            'type': 'string'
                        },
                        "manufactureyear": {
                            'type': 'string'
                        },
                        "mpov": {
                            'type': 'string'
                        },
                        "technicalfailure": {
                            'type': 'string'
                        },
                        "ownershipform": {
                            'type': 'string'
                        },
                        "legalform": {
                            'type': 'string'
                        },
                        "vehicleparticipant": {
                            'type': 'list',
                            'default': [],
                            'schema': {
                                "category": {
                                    'type': 'string'
                                },
                                "directviolationsror": {
                                    'type': 'list'
                                },
                                "severity": {
                                    'type': 'string'
                                },
                                "sex": {
                                    'type': 'string'
                                },
                                "srivingexperience": {
                                    'type': 'string'
                                },
                                "intoxicationdegree": {
                                    'type': 'string'
                                },
                                "relatedviolationsror": {
                                    'type': 'list'
                                },
                                "usesafetybelt": {
                                    'type': 'string'
                                },
                                "leaveta": {
                                    'type': 'string'
                                },
                                "numberparticipant": {
                                    'type': 'string'
                                },
                                "seatgroup": {
                                    'type': 'string'
                                },
                                "injuredcardid": {
                                    'type': 'string'
                                },
                            }
                        }
                    }
                },
                "humansettlement": {
                    'type': 'string'
                },
                "street": {
                    'type': 'string'
                },
                "house": {
                    'type': 'string'
                },
                "roadname": {
                    'type': 'string'
                },
                "km": {
                    'type': 'string'
                },
                "m": {
                    'type': 'string'
                },
                "streetcategory": {
                    'type': 'string'
                },
                "roadcategory": {
                    'type': 'string'
                },
                "roadimportance": {
                    'type': 'string'
                },
                "factor": {
                    'type': 'list'
                },
                "weathercondition": {
                    'type': 'list'
                },
                "carriagewaycondition": {
                    'type': 'string'
                },
                "lighting": {
                    'type': 'string'
                },
                "changesmovementmode": {
                    'type': 'string'
                },
                "tacarriagewaycondition": {
                    'type': 'string'
                },
                "latitude": {
                    'type': 'string'
                },
                "longitude": {
                    'type': 'string'
                },
                "objectsta": {
                    'type': 'list'
                },
                "participantinfo": {
                    'type': 'list',
                    'default': [],
                    'schema': {
                        "category": {
                            'type': 'string'
                        },
                        "directviolationsror": {
                            'type': 'list'
                        },
                        "severity": {
                            'type': 'string'
                        },
                        "sex": {
                            'type': 'string'
                        },
                        "srivingexperience": {
                            'type': 'string'
                        },
                        "intoxicationdegree": {
                            'type': 'string'
                        },
                        "relatedviolationsror": {
                            'type': 'list'
                        },
                        "usesafetybelt": {
                            'type': 'string'
                        },
                        "leaveta": {
                            'type': 'string'
                        },
                        "numberparticipant": {
                            'type': 'string'
                        },
                        "seatgroup": {
                            'type': 'string'
                        },
                        "injuredcardid": {
                            'type': 'string'
                        }
                    }
                }
            }
        }
    }
}