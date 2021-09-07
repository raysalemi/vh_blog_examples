import cocotb
from cocotb.queue import T
from pyuvm import *;

class txn_a(uvm_transaction):
    def __init__(self, name, val):
        super().__init__(name)
        self.value = val

class txn_b(uvm_transaction):
    def __init__(self, name, val):
        super().__init__(name)
        self.value = val

class test(uvm_test):
    def build_phase(self):
        self.int_fifo = uvm_tlm_fifo("int_fifo", self)
        self.put_port = uvm_put_port("put_port", self)
        self.get_port = uvm_get_port("get_port", self)
    
    def connect_phase(self):
        self.put_port.connect(self.int_fifo.put_export)
        self.get_port.connect(self.int_fifo.get_export)

    def end_of_elaboration_phase(self):
        self.set_logging_level_hier(logging.NOTSET)

    async def run_phase(self):
        self.raise_objection()
        aa = txn_a("aa", 5)
        await self.put_port.put(aa)
        aa = await self.get_port.get()
        self.logger.info(f"Got aa.value = {aa.value}")
        self.drop_objection()

@cocotb.test()
async def run_test(dut):
    await uvm_root().run_test("test")
    assert True
        