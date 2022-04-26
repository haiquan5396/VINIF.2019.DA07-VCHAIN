import asyncio

from settings import config
from utils.logging import get_logger
from database import Database
from utils.broker_client import BrokerClient
from dapp.event_handler import DappHandler
from network.event_handler import NetworkHandler

_LOGGER = get_logger(__name__)


class FabricDriver:
    def __init__(self, driver_config):
        self.database = Database(
            host=driver_config["database"]["host"],
            port=driver_config["database"]["port"],
            username=driver_config["database"]["username"],
            password=driver_config["database"]["password"],
            dbname=driver_config["database"]["db_name"],
        )

        self.broker_client = BrokerClient(
            username=driver_config["rabbitmq"]["username"],
            password=driver_config["rabbitmq"]["password"],
            host=driver_config["rabbitmq"]["host"],
            port=driver_config["rabbitmq"]["port"],
        )
        self.network_handler = NetworkHandler(
            database=self.database, broker_client=self.broker_client
        )

        self.dapp_handler = DappHandler(
            database=self.database, broker_client=self.broker_client
        )

    async def setup_service(self, loop):
        await self.database.connect()

        event_handlers = {
            "driver.fabric.request.create_network": self.network_handler.handle_create_network,
            "driver.fabric.request.retry_create_network": self.network_handler.handle_retry_create_network,
            "driver.fabric.request.update_network": self.network_handler.handle_update_network,
            "driver.fabric.request.retry_update_network": self.network_handler.handle_retry_update_network,
            "driver.fabric.request.rollback_update_network": self.network_handler.handle_rollback_update_network,
            "driver.fabric.request.delete_network": self.network_handler.handle_delete_network,
            "driver.fabric.request.network_error": self.network_handler.handle_network_error,
            "driver.fabric.request.create_resource": self.network_handler.handle_create_resource,
            "driver.fabric.request.create_dapp": self.dapp_handler.handle_create_dapp,
            "driver.fabric.request.retry_create_dapp": self.dapp_handler.handle_retry_dapp,
            "driver.fabric.request.update_dapp": self.dapp_handler.handle_update_dapp,
            "driver.fabric.request.retry_update_dapp": self.dapp_handler.handle_retry_dapp,
            "driver.fabric.request.rollback_update_dapp": self.dapp_handler.handle_rollback_dapp,
            "driver.fabric.request.delete_dapp": self.dapp_handler.handle_delete_dapp,
            "driver.fabric.request.retry_delete_dapp": self.dapp_handler.handle_delete_dapp,
            "driver.fabric.request.dapp_error": self.dapp_handler.handle_dapp_error,
        }
        loop.create_task(
            self.broker_client.consume("fabric.coreservice.events", event_handlers)
        )

    async def close_connection(self):
        await self.broker_client.close()
        # await self.database


driver = FabricDriver(config)
loop = asyncio.get_event_loop()
loop.run_until_complete(driver.setup_service(loop))
try:
    loop.run_forever()
finally:
    loop.run_until_complete(driver.close_connection())
    _LOGGER.debug("Driver stopped")

loop.close()
# asyncio.run(setup_service(config))
