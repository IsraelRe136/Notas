/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package yoRobot;

/**
 *
 * @author resen
 */

public class hadron extends Personaje{
    private boolean visible=true;

    public hadron() {
    }
    
    
    public boolean cambioVisibilidad(){
        if(visible) visible = false;
        else visible = true;
        return visible;
    }
    
    
}
