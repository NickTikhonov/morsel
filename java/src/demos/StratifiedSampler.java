package demos;

import java.util.ArrayList;

import com.nicktikhonov.morsel.stratified_sampler.Field;
import com.nicktikhonov.morsel.stratified_sampler.Vector;

public class StratifiedSampler {

	public static void main(String[] args){
        double x1 = Double.parseDouble(args[0]);
        double y1 = Double.parseDouble(args[1]);

        double x2 = Double.parseDouble(args[2]);
        double y2 = Double.parseDouble(args[3]);

        double x3 = Double.parseDouble(args[4]);
        double y3 = Double.parseDouble(args[5]);

        double x4 = Double.parseDouble(args[6]);
        double y4 = Double.parseDouble(args[7]);

        int numDivisions = Integer.parseInt(args[8]);
        int numSamples = Integer.parseInt(args[9]);

		Field demo = new Field(
					new Vector(x1, y1),
					new Vector(x2, y2),
					new Vector(x3, y3),
					new Vector(x4, y4)
				);

		demo.generateRects(numDivisions, numSamples); //Generate a field with 2x2 strata grid

		ArrayList<Vector> samples = demo.getSamples();

        System.out.print("{ samples: [");

        for(int i = 0; i < samples.size(); i++){
		    System.out.print(samples.get(i).toString());
		    if(i + 1 < samples.size())
		        System.out.print(", ");
        }

		System.out.println(" ]}");
	}

}
