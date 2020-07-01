''' ---------------------------------------------------------------------------
Description:    This script parses an html local file ( a gcp practice exam )
                and return as output your score

--------------------------------------------------------------------------- '''
import argparse
import os.path
import pathlib
import re
import sys
import time
import ws_utils
from   bs4 import BeautifulSoup as bs


class Gcp_test_grader:
    #file_path = 'C:/aat/prg/web_scraping_01/data/exam2020-05-22.html'
    file_path = 'C:/aat/prg/web_scraping_01/data/2020-06-30_000.html'

    right_answers = 0
    wrong_answers = 0
    score = 0.0

    def get_right_answers( self, soup ):
        '''
        use the beautiful soup object, scrape the web page return the number of right answers.
        :param soup:
        :return:
        '''
        try:
            my_dic = {  'aria-label': 'Correct',
                        'class' : 'freebirdFormviewerViewItemsItemCorrectnessIcon'
                     }
            questions  = soup.find_all('div', my_dic )
            self.right_answers = len( questions )

            '''i = 1
            for q in questions:
                print( 'i:{}  q:{}'.format( i, q.attrs[ 'id' ] ) )
                i = i +1'''

        except Exception as e:
            error_msg = sys.exc_info()[0]
            print( 'Gcp_test_grader.get_right_answers(), row_num: {}, error: {}'.format( row_num, error_msg ) )
            raise

    def get_wrong_answers( self, soup ):
        '''
        use the beautiful soup object, scrape the web page return the number of wrong answers.
        :param soup:
        :return:
        '''
        try:
            my_dic = {  'aria-label': 'Incorrect',
                        'class' : 'freebirdFormviewerViewItemsItemCorrectnessIcon'
                     }
            questions  = soup.find_all('div', my_dic )
            self.wrong_answers = len( questions )

            '''i = 1
            for q in questions:
                print( 'i:{}  q:{}'.format( i, q.attrs[ 'id' ] ) )
                i = i + 1'''

        except Exception as e:
            error_msg = sys.exc_info()[0]
            print( 'Gcp_test_grader.get_wrong_answers(), row_num: {}, error: {}'.format( row_num, error_msg ) )
            raise

    def print_results(self):
        self.score = 100.0 * self.right_answers  / (self.right_answers + self.wrong_answers)
        print( '\n\n\n' + '-' * 80 )
        print('File          : {}'.format( self.file_path     ) )
        print( 'right answers: {}'.format( self.right_answers ) )
        print( 'wrong answers: {}'.format( self.wrong_answers ) )
        print( 'score        : {}'.format( self.score         ) )

        if self.score == 100.0:
            print( 'You Win, PERFECT !! Now you are Ready.' )
        elif self.score >= 97.0:
            print( 'You can you to the real exam' )
        elif self.score > 95.0:
            print( 'Congratualitions, you are in good shape' )
        else:
            print( 'Come on Einstain, study double :D' )

        print( '-' * 80 + '\n\n\n' )

    def run( self ):

        try:
            soup = bs( open( self.file_path ), "html.parser")
            self.get_right_answers( soup )
            self.get_wrong_answers( soup )
            self.print_results()

        except Exception as e:
            error_msg = sys.exc_info()[0]
            print( '\n\n Test_grader.run(), error: {}'.format( error_msg) )
            raise

    def __init__(self, file_path):
        if file_path != None:
            self.file_path = file_path


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument( '--file_path', help="Score a practice test. The file must an html. Usage: python Gcp_test_grader.py data/2020-06-30_000.html")
        args = parser.parse_args()
        #print( 'File: {}'.format( args.file_path ) )

        gcp_test_grader = Gcp_test_grader( args.file_path )
        gcp_test_grader.run()

    except Exception as e:
        error_msg = sys.exc_info()[0]
        print('error: {}'.format(error_msg))




