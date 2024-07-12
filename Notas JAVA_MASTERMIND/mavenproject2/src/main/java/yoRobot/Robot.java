/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package yoRobot;

/**
 *
 * @author resen
 */
public class Robot {
    
    private float peso;
    
    Pieza sinIdentificacion;
    CPU cpu;
    BATERIA bateria;
    

    public Robot() {
        this.sinIdentificacion = sinIdentificacion;
        this.cpu = new CPU();
        this.cpu.setNumSerie("csadc");
        this.bateria = new BATERIA();
        this.bateria.setPeso(250);
    }

    public void setPeso(float peso) {
        this.peso = peso;
    }

    public float getPeso() {
        return peso;
    }
    
    
    
    

    
    
}
