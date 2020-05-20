using System;
using System.Text;
namespace KnightsTour{
    class Tour{
        public int[,] board=
        {
            {-1,-1,-1,-1,-1,-1,-1,-1},
            {-1,-1,-1,-1,-1,-1,-1,-1},
            {-1,-1,-1,-1,-1,-1,-1,-1},
            {-1,-1,-1,-1,-1,-1,-1,-1},
            {-1,-1,-1,-1,-1,-1,-1,-1},
            {-1,-1,-1,-1,-1,-1,-1,-1},
            {-1,-1,-1,-1,-1,-1,-1,-1},
            {-1,-1,-1,-1,-1,-1,-1,-1}
        };

        private int current{get;set;}
        public Tour(){
            current = 1;
        }
        private void SolveTourHelper(int row, int col){
            if(row < 0 || row >7){
                return;
            }
            if(col < 0 || col > 7){
                return;
            }
            if(board[row,col] != -1){
                return;
            }
            board[row,col] = this.current;
            this.current++;
            SolveTourHelper(row-2,col-1);
            SolveTourHelper(row-2,col+1);
            SolveTourHelper(row-1,col+2);
            SolveTourHelper(row+1,col+2);
            SolveTourHelper(row+2,col+1);
            SolveTourHelper(row+2,col-1);
            SolveTourHelper(row+1,col-2);
            SolveTourHelper(row-1,col-2);
        }
        public void SolveTour(){
            SolveTourHelper(0,0);
        }

        public override String ToString(){
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < 8; i++){
                for(int j = 0; j < 8; j++){
                    sb.Append(this.board[i,j].ToString().PadRight(3));
                }
                sb.Append("\n");
            }
            return sb.ToString();
        }
        public static void Main(string[] args){
            Tour test = new Tour();
            test.SolveTour();
            Console.WriteLine(test);
        }
    }
}
