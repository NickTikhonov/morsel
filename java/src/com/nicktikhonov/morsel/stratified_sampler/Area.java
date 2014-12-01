package com.nicktikhonov.morsel.stratified_sampler;

import java.util.ArrayList;
import java.util.Random;

public class Area {

	private Vector v1, v2, v3, v4;
	private ArrayList<Vector> samplePoints;

	public Area(Vector v1, Vector v2, Vector v3, Vector v4, int numSamples){
		samplePoints = new ArrayList<Vector>();

		this.v1 = v1;
		this.v2 = v2;
		this.v3 = v3;
		this.v4 = v4;

		generateSamples(numSamples);
	}

	public void generateSamples(int numSamples){
		samplePoints.clear();
		Triangle t1 = new Triangle(v1, Vector.sub(v2, v1), Vector.sub(v4, v1));
		Triangle t2 = new Triangle(v3, Vector.sub(v2, v3), Vector.sub(v4, v3));

		Random r = new Random();
		for(int i = 0; i < numSamples; i++){
			if(r.nextBoolean()){
				samplePoints.add(t1.getPointInside(r));
			}else{
				samplePoints.add(t2.getPointInside(r));
			}
		}
	}
	
	public ArrayList<Vector> getSamples(){
		return samplePoints;
	}

}
