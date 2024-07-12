/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package yoRobot;

/**
 *
 * @author resen
 */
public class Habitacion {
    
    public static final int Ancho=10;
    public static final int Alto=10;
    
    private Posicion puertaEntrada;
    private Posicion puertaSalida;
    
    private Personaje j;

    public void setJ(Personaje j) {
        this.j = j;
    }
 

   

    public Habitacion() {
        System.out.println("1");
    }

    public Posicion getPuertaEntrada() {
        return puertaEntrada;
    }

    public void setPuertaEntrada(Posicion puertaEntrada) {
        this.puertaEntrada = puertaEntrada;
    }

    public Posicion getPuertaSalida() {
        return puertaSalida;
    }

    public void setPuertaSalida(Posicion puertaSalida) {
        this.puertaSalida = puertaSalida;
    }
    
    public boolean esunaPuerta (Posicion p){
        if(p.esIgual(puertaEntrada) || p.esIgual(puertaSalida)  ) return true;
        else return false;
    }
    
    
    
}
