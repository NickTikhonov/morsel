package com.nicktikhonov.morsel.stratified_sampler;

import java.util.Random;

public class Triangle {

	private Vector origin;
	private Vector r1, r2;

	public Triangle(Vector origin, Vector r1, Vector r2){
		this.origin = origin;
		this.r1 = r1;
		this.r2 = r2;
	}

	public Vector getPointInside(Random r){
		double b1 = r.nextDouble();
		double b2 = r.nextDouble();

		Vector vec;
		Vector randomAdd;

		while(true){
			randomAdd = Vector.sum(Vector.multConst(r1, b1), Vector.multConst(r2, b2));
			vec = Vector.sum(origin, randomAdd);

			if(isInsideTriangle(vec, origin, Vector.sum(origin, r1), Vector.sum(origin, r2))){
				return vec;
			}

			b1 = r.nextDouble();
			b2 = r.nextDouble();
		}
	}

	boolean isInsideTriangle(Vector s, Vector a, Vector b, Vector c)
	{
	    double as_x = s.x-a.x;
	    double as_y = s.y-a.y;

	    boolean s_ab = (b.x-a.x)*as_y-(b.y-a.y)*as_x > 0;

	    if((c.x-a.x)*as_y-(c.y-a.y)*as_x > 0 == s_ab) return false;

	    if((c.x-b.x)*(s.y-b.y)-(c.y-b.y)*(s.x-b.x) > 0 != s_ab) return false;

	    return true;
	}

}
