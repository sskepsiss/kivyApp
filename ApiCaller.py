from SettingsService import SettingsService
import requests

class ApiCaller():
    '''
    Author: Marian Neff
    -------------------
    The ApiCaller is a service that is used to communicate with the Tankerkoenig API. The api returns all the different petrol stations within a chosen radius around the user's location.
    The class constants KEY and URL are used to put together the correct API url.
    -------------------
    '''

    KEY = '1e89035b-ed46-fdc3-4baf-feff2614dc10'
    URL = 'https://creativecommons.tankerkoenig.de/json/list.php'

    def __init__(self, settingsService):
        '''
        Sets the required dependencies for the class
        -------------------
        Parameters:
            settingsService: SettingsService, 
        -------------------
        Returns:
            void
        -------------------
        '''

        assert isinstance(settingsService, SettingsService)
        self.__settingsService = settingsService

    def getQueriedTankerData(self):
        '''
        Uses the provided location values to query the Tankerkoenig API and get back matching values. The settings and the location values for the API call are loaded through the SettingsService class.
        -------------------
        Parameters:
            none
        -------------------
        Returns:
            dictionary
        -------------------
        '''

        try: 
            settings = self.__settingsService.loadSettings()
            (lat, long) = self.__settingsService.loadLocationSettings()
            url = self.URL + "?lat=" + str(lat) + '&lng=' + str(long) + '&rad=' + str(settings.get('radius')) + '&sort=dist&type=' + settings.get('type') + '&apikey=' + self.KEY
            data = requests.get(url)

            return data.json()
        except Exception as error:
            print(f'An error has occurred during the API call, message: {error}')

            return { "stations": [] }