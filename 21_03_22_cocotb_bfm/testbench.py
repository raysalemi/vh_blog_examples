import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge
from tinyalu_utils import TinyAluBfm


@cocotb.test()
async def test_alu(dut):
    clock = Clock(dut.clk, 2, units="us")
    cocotb.fork(clock.start())
    bfm = TinyAluBfm(dut)
    await bfm.startup_bfms()
    await FallingEdge(dut.clk)
    await bfm.send_op(0xAA, 0x55, 1)
    await cocotb.triggers.ClockCycles(dut.clk, 5)
    cmd = await bfm.get_cmd()
    result = await bfm.get_result()
    print("cmd:", cmd)
    print("result:", result)
    assert result == 0xFF
