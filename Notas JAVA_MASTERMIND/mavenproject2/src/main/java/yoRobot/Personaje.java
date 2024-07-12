/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package yoRobot;

/**
 *
 * @author resen
 */
public class Personaje {
    private String nombre;
    private int poX;
    private int posY;

    Posicion pos;

    public Posicion getPos() {
        return pos;
    }

    public void setPos(Posicion pos) {
        this.pos = pos;
    }
    
    public String getNombre() {
        return nombre;
    }





     public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setPoX(int poX) {
        this.poX = poX;
    }

    public void setPosY(int posY) {
        this.posY = posY;
    }
    
    public Personaje() {
        System.out.println("xswa");
    }
    
}
