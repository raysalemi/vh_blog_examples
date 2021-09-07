import uvm_pkg::*;
`include "uvm_macros.svh"

class txn_a extends uvm_transaction;
    int value;
    function new(string name, int val);
       value = val;
    endfunction
endclass

class txn_b extends uvm_transaction;
    int value;
    function new(string name, int val);
       value = val;
    endfunction
endclass

class test extends uvm_test;
`uvm_component_utils(test)
    uvm_tlm_fifo #(txn_a) int_fifo;
    uvm_put_port #(txn_a) put_port;
    uvm_get_port #(txn_b) get_port;

    function new(string name = "test", uvm_component parent=null);
        super.new(name, parent);
    endfunction

    function void build_phase(uvm_phase phase);
        int_fifo = new("int_fifo", this);
        put_port = new("int_put", this);
        get_port = new("int_get", this);
    endfunction

    function void connect_phase(uvm_phase phase);
        put_port.connect(int_fifo.put_export);
        get_port.connect(int_fifo.get_export);
    endfunction

    task run_phase(uvm_phase phase);
        txn_a aa;
        txn_b bb;
        aa = new("aa", 5);
        phase.raise_objection(this);
        put_port.put(aa);
        get_port.get(bb);
        $display("bb: %0d", bb.value);
        phase.drop_objection(this);
    endtask
endclass

module run();
    initial
        run_test("test");
endmodule

        

