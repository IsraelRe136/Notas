/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package yoRobot;

import java.sql.SQLOutput;

/**
 *
 * @author resen
 */
public class Juego {
    public Juego(){
        
    }
    
    public static void pintarHabitacion(Habitacion h) {
        System.out.println("pintamos l ahbitacion");
        
        for(int fil=0; fil<Habitacion.Alto;fil++){
            for(int col=0;col<Habitacion.Ancho;col++){
                Posicion posicionActual= new Posicion(col, fil);
                if( h.esunaPuerta(posicionActual)) System.out.print(" ");
                if(col==0 || col==Habitacion.Ancho-1) System.out.print("|");
                else if (fil==0 || fil==Habitacion.Alto-1)System.out.print("=");
                else System.out.print(" ");
                
                if(col==Habitacion.Ancho-1)System.out.println();
            
        }
        
    }
    }     
}
