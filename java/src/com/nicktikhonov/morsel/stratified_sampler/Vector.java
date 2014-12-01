package com.nicktikhonov.morsel.stratified_sampler;

public class Vector{

	public double x;
	public double y;

	public Vector(double x, double y){
		this.x = x;
		this.y = y;
	}

	public double getLength(){
		return Math.sqrt(x*x + y*y);
	}

	public void add(Vector other){
		this.x += other.x;
		this.y += other.y;
	}

	public static Vector sum(Vector s1, Vector s2){
		return new Vector(s1.x + s2.x, s1.y + s2.y);
	}

	public static Vector sub(Vector s1, Vector s2){
		return new Vector(s1.x - s2.x, s1.y - s2.y);
	}

	public static Vector inverse(Vector vec){
		return new Vector(-vec.x, -vec.y);
	}

	public static Vector multConst(Vector vec, double length){
		return new Vector(vec.x * length, vec.y * length);
	}

	public static Vector scale(Vector vec, double length){
		return multConst(vec, length/vec.getLength());
	}

	public String toString(){
		return "{ x: " + x + ", y: " + y + " }";
	}
}
