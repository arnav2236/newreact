import React, { Component } from 'react';
import { Card, CardImg, CardImgOverlay, CardText ,CardBody, CardTitle}  from 'reactstrap';
class Menu extends Component {
    constructor(props) {
        super(props);

        this.state={

        } 



    }

    render() {
// we changes this.state to this.props to make it use the state from its ancestral component not from 
// state of current component
        const menu=this.props.dishes.map((dish)=>{

            return (
                <div key={dish.id} className="col-12 col-md-5 m-1">
                    <Card>
                        <Media left middle>
                            <Media object src={dish.image} alt={dish.name} />
                        </Media>
                        <Media body className="ml-5">
                            <Media heading>{dish.name}</Media>
                            <p>{dish.description}</p>
                        </Media>
                    </Card>
                </div>
            )
        })
        return (
            <div className="container">
                <div className='row'>
                    <Media list>
                        {menu}
                    </Media>``
                    
                </div>
            </div>



        );
    }
}

export default Menu;