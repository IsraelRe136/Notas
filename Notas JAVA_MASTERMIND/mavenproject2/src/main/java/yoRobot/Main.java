/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package yoRobot;

import jdk.jfr.Percentage;

/**
 *
 * @author resen
 */
public class Main {
    public static void main(String[] args) {
        Posicion posInicial= new Posicion(3,0);
        
      //  Posicion posInicial= new Posicion();
       // posInicial.setPosX(3);
      //  posInicial.setPosY(0);

       Habitacion hab1= new Habitacion();
       
       Personaje jugador=new Personaje();
       
       jugador.setPos(posInicial);
       
       
       
               
       Juego.pintarHabitacion(hab1);
       
    
      
       
    }
}
