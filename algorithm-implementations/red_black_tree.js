/*
 * Red Black Tree implementation as specified in CLRS
 * However, I changed the colors to red and green so I could be festive 
 */
const Colors = {'RED': 0, 'GREEN': 1};

class Node{
    constructor(value, color, left=null, right=null, parent=null){
        this.value = value;
        this.color = color;
        this.left = left;
        this.right = right;
        this.parent = parent;
    };
}

class RedGreenTree{
    constructor(root=null){
        this.root = root;
    };

    leftRotate = (x) => {
        let y = x.right;
        x.right = y.left;
        if(y.left){
            y.left.parent = x
        }
        y.parent = x.parent;
        if(!x.parent){
            this.root = y;
        }
        else if(x == x.parent.left){
            x.parent.left = y;
        }
        else{
            x.parent.right = y
        }
        y.left = x;
        x.parent = y;
    }

    rightRotate = (x) => {
        let y = x.left;
        x.left = y.right;
        if(y.right){
            y.right.parent = x;
        }
        y.parent = x.parent
        if(!x.parent){
            this.root = y;
        }
        else if(x == x.parent.left){
            x.parent.left = y ;
        }
        else{
            x.parent.right = y;
        }
        y.right = x;
        x.parent = y;
    }

    fixup = (z) =>{
        var y;
        while(z.parent && z.parent.color == Colors.RED){
            if(z.parent.parent && z.parent == z.parent.parent.left){
                y = z.parent.parent.right;
                if(y && y.color == Colors.RED){
                    z.parent.color = Colors.GREEN;
                    y.color = Colors.GREEN;
                    z.parent.parent.color = Colors.RED;
                    z = z.parent.parent;
                }
                else{
                    if(z == z.parent.right){
                        z = z.parent;
                        this.leftRotate(z);
                    }
                    z.parent.color = Colors.GREEN;
                    z.parent.parent.color = Colors.RED;
                    this.rightRotate(z.parent.parent);
                }
            }
            else{
                y = z.parent.parent.left;
                if(y && y.color == Colors.RED){
                    z.parent.color = Colors.GREEN;
                    y.color = Colors.GREEN;
                    z.parent.parent.color = Colors.RED;
                    z = z.parent.parent;
                }
                else{
                    if(z == z.parent.left){
                        z = z.parent;
                        this.rightRotate(z);
                    }
                    z.parent.color = Colors.GREEN;
                    z.parent.parent.color = Colors.RED;
                    this.leftRotate(z.parent.parent);
                }
            }
        }
        this.root.color = Colors.GREEN;
    }

    insert = (value) => {
        let z = new Node(value, Colors.RED)
        let y = null;
        let x = this.root;
        while(x != null){
            y = x;
            x = value < x.value ? x.left : x.right;
        }
        z.parent = y
        if(y == null){
            this.root = z;
        }
        else if(z.value < y.value){
            y.left = z;
        }
        else{
            y.right = z;
        }
        this.fixup(z);
    };

    toStringHelper = (root, level) =>{
        if(!root){
            return "-".repeat(level*2) + "None";
        }
        let S = ""
        S += "-".repeat(level*2) + `(${root.value}, ${root.color == Colors.RED ? "Red" : "Green"})\n`;
        S += this.toStringHelper(root.left, level+1) + '\n';
        S += this.toStringHelper(root.right, level+1);
        return S
    }

    toString = () =>{
        return this.toStringHelper(this.root, 0)
    }
}

function main(){
    let rgtree = new RedGreenTree()
    for(const arg of Deno.args){
        rgtree.insert(arg);
    }
    console.log(rgtree.toString());
};
main()
