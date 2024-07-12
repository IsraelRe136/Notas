/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package yoRobot;

/**
 *
 * @author resen
 */


public class Posicion {
     private int posX;
     private int posY;

    public int getPosX() {
        return posX;
    }

    public void setPosX(int posX) {
        this.posX = posX;
    }

    public int getPosY() {
        return posY;
    }

    public void setPosY(int posY) {
        this.posY = posY;
    }
     
     
    public Posicion() {
        this.posX=0;
        this.posY=0;
      
    }
    
    public Posicion( int posx, int posy) {
        this.posX=0;
        this.posY=0;
      
    }
    
    public boolean esIgual(Posicion p){
     if(p.posX==this.posX && p.posY==this.posY   ) return true;
     else return false;
    }
    
}
