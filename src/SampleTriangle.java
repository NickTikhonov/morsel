import java.util.Random;

public class SampleTriangle {

	private SampleVector origin;
	private SampleVector r1, r2;

	public SampleTriangle(SampleVector origin, SampleVector r1, SampleVector r2){
		this.origin = origin;
		this.r1 = r1;
		this.r2 = r2;
	}

	public SampleVector getPointInside(Random r){
		double b1 = r.nextDouble();
		double b2 = r.nextDouble();

		SampleVector vec;
		SampleVector randomAdd;

		while(true){
			randomAdd = SampleVector.sum(SampleVector.multConst(r1, b1), SampleVector.multConst(r2, b2));
			vec = SampleVector.sum(origin, randomAdd);

			System.out.println("Stuck");
			if(intpoint_inside_trigon(vec, origin, SampleVector.sum(origin, r1), SampleVector.sum(origin, r2))){
				return vec;
			}

			b1 = r.nextDouble();
			b2 = r.nextDouble();
		}
	}

	boolean intpoint_inside_trigon(SampleVector s, SampleVector a, SampleVector b, SampleVector c)
	{
	    double as_x = s.x-a.x;
	    double as_y = s.y-a.y;

	    boolean s_ab = (b.x-a.x)*as_y-(b.y-a.y)*as_x > 0;

	    if((c.x-a.x)*as_y-(c.y-a.y)*as_x > 0 == s_ab) return false;

	    if((c.x-b.x)*(s.y-b.y)-(c.y-b.y)*(s.x-b.x) > 0 != s_ab) return false;

	    return true;
	}

}
