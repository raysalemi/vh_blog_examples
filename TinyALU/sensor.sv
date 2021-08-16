
class data;
   rand int sample;
   constraint example {sample >=50; sample <=80;}
endclass 

module sensor_reader();
    int samples[0:9];

    task data_from_sensor(output int sample);
        data datum;
        datum = new();
        datum.randomize()
        #1;
        sample = datum.sample;
        $display(sample)
    endtask

    task gather_ten_samples();
        int unsigned sample;
        for (int ii = 0; ii < 10; ii++) begin
            data_from_sensor(sample);
            samples[ii] = datum.sample
        end
        $write("[ ");
        for (ii = 0; ii < 10; ii++) begin
            $write("%0d, ", samples[ii]);
        end
        $write("]");
    endtask

    initial
        gather_ten_samples();

