//filename: exercise_one.go
package go_unit_test_bootcamp

func FindMissingDrone(droneIds []int) int {
    result := 0
	//loop through array of droneIds and XOR each element
    for _, id := range droneIds {
        result ^= id
    }
	return result
}