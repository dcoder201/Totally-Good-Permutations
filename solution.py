from itertools import permutations
def totally_good(alphabet, bads):
    n = len(alphabet)
    perms = permutations(alphabet)
    bad_set = set(bads)
    count = 0
    for perm in perms:
        perm_str = ''.join(perm)
        is_good = all(sub not in perm_str for sub in bad_set)
        if is_good:
            count += 1
    return count
  
  
  
from solution import totally_good
import codewars_test as test

# All of these Fixed tests have been validated by comparing them to brute force counting of all possible permutations

@test.describe("Fixed tests")
def tests():
    
    @test.it("Should obtain correct number of totally good permutations for the most basic inputs")
    def test_totally_good_basic_small():
        test.assert_equals(totally_good('ABC',[]),6)
        test.assert_equals(totally_good('ABCD',[]),24)
        test.assert_equals(totally_good('ABCDE',[]),120)
        test.assert_equals(totally_good('ABCD',['AB']),18)
        test.assert_equals(totally_good('ABCD',['BA']),18)
        test.assert_equals(totally_good('ABCD',['A']),0)
        test.assert_equals(totally_good('ABC',['AB','CA']),3)

    @test.it("Should obtain correct number of totally good permutations for some simple inputs")
    def test_totally_good_simple_small():
        test.assert_equals(totally_good('ABCD',['A','BC']),0)
        test.assert_equals(totally_good('ABCD',['AB','CD']),14)
        test.assert_equals(totally_good('ABCDE',['AB','CD']),78)
        test.assert_equals(totally_good('ABCDE',['AB','CDE']),92)
        
    @test.it("Should obtain correct number of totally good permutations for first signs of complexity")
    def test_totally_good_first_complex():
        test.assert_equals(totally_good('ABCD',['A','AC']),0)
        test.assert_equals(totally_good('ABCDE',['AB','BC']),78)
        test.assert_equals(totally_good('ABCDE',['ABC','BE']),90)
        test.assert_equals(totally_good('ABCDEF',['FC','CAE']),582)
        test.assert_equals(totally_good('ABCDEF',['FC','BC','EC']),360)
        test.assert_equals(totally_good('ABCDEF',['FC','BC','EC','BE']),288)
        test.assert_equals(totally_good('ABCDEFGH',['FC','ABD','EHG']),34098)
        test.assert_equals(totally_good('ABCDEFGH',['ABCD','BCDE']),40104)
        test.assert_equals(totally_good('ABCDEFGH',['ABCD','BCDEFG']),40196)
        
    @test.it("Should obtain correct number of totally good permutations for slightly more complexity")
    def test_totally_good_second_complex():
        test.assert_equals(totally_good('ABCDE',['ABC','CD','DEA']),89)
        test.assert_equals(totally_good('ABCDEFGH',['ABCD','CDEFG','FGH']),39469)
        test.assert_equals(totally_good('ABCDEFGH',['AB','BCD','CDE','DEFG','GH']),29966)
        test.assert_equals(totally_good('ABCDEFGH',['ABCD','CDEF','EFGH','GHAB']),39864)

    @test.it("Should obtain correct number of totally good permutations for a bit more complexity")
    def test_totally_good_third_complex():
        test.assert_equals(totally_good('ABCDE',['ABC','BE','ADC']),86)
        test.assert_equals(totally_good('ABCDE',['ABC','BE','EA','CB']),60)
        test.assert_equals(totally_good('ABCDEFGH',['AB','BC','FG','GH']),24024)
        test.assert_equals(totally_good('ABCDEFGH',['AB','BC','CDE','FG','GH']),23662)
        test.assert_equals(totally_good('ABCDEFGH',['ABC','CD','DEFG','FGH']),34023)
        
    @test.it("Should obtain correct number of totally good permutations for tricky cases")
    def test_totally_good_tricky_cases():
        test.assert_equals(totally_good('ABCDEFGH',['ABCDE','BCD']),39600)
        test.assert_equals(totally_good('ABCDEFGH',['ABCDEF','BCDE','DE']),35280)
        test.assert_equals(totally_good('ABCDEFGH',['ABCDEF','BCDEF','BCDE','CDE','DE']),35280)
        test.assert_equals(totally_good('ABCDEFGH',['ABH','CH','DEH','FGH']),33120)
        test.assert_equals(totally_good('ABCDEFGH',['ABH','CBH','DEBH','FGBH']),38640)
        
    @test.it("Should obtain correct number of totally good permutations for more tricky cases")
    def test_totally_good_more_tricky_cases():
        test.assert_equals(totally_good('ABCDEFG',['BCDE','CE','CF','CB','EB']),2376)
        test.assert_equals(totally_good('ABCDEFGH',['AB','BC','CDE','BCD','DEFG','GH']),26761)
        test.assert_equals(totally_good('ABCDEFGH',['AB','BC','CDE','BCD','DEFG','GH','EF']),23662)
        test.assert_equals(totally_good('ABCDEFGH',['AB','BC','CDE','BCD','DEFG','GH','EF','HCBG']),23566)
        test.assert_equals(totally_good('ABCDEFGH',['AB','BC','CDE','BCD','DEFG','GH','EF','HCBG','CB']),19942)
        test.assert_equals(totally_good('ABCDEFGH',['BCDEFG','CDEF','DE','BCD','EFG','CD','EF','FEDC','ABC','ABCD']),26694)
        test.assert_equals(totally_good('ABCDEFGH',['ABC','ACB','BAC','BCA','CAB','CBA']),36000)
        
    @test.it("Should obtain correct number of totally good permutations for larger and larger alphabets - IMPORTANT NOTE there are 2 EXTRA commented test cases here in Sample Tests that will fail with brute force approaches: you can un-comment them when you think your solution is performant enough")
    def test_totally_good_larger_alphabets():
        test.assert_equals(totally_good('ABCDEFGHIJKL',[]),479001600)
        test.assert_equals(totally_good('ABCDEFGHI',['AB','CD','EFGH','BC','FG','BH','ABCDE','DAC','ADG','IFBC']),194520)
        test.assert_equals(totally_good('ABCDEFGHI',['ABCDEF','CDFIBA','HIFDCA','GHFCAB','ABCDIHG','EFGCDA','IHEFDCA','HAIE','FEBHDA','ACHIEBF','CE','BADICE']),321678)
        test.assert_equals(totally_good('ABCDEFGHIJ',['AB','CD','EFGH','BC','FG','BH','ABCDE','DAC','ADG','IFBC']),2082240)
        # brute force will take about 20 seconds on below test case, your solution should work on it if you want to pass the full tests
        #test.assert_equals(totally_good('ABCDEFGHIJK',['AB','CD','EFGH','BC','FG','BH']),24766560)
        # checked this one with brute force as well, it takes ~400 seconds, answer matches reference solution OK!
        #test.assert_equals(totally_good('ABCDEFGHIJKL',['IFLKE','DGLEJ','LGACFIKBDJ','JL','EI','FCBIEHDGJK','IEFHLJDCKAG','KC','GBACLFJKHEI']),369699106)
